import pandas as pd
import sqlite3
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = Path(r"C:\Users\david\OneDrive\Pictures\Documentos\data_analyst\project_students\StudentPerformanceFactors.csv")
DB_PATH = BASE_DIR / "students.db"


def extract_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")

    logger.info("Extrayendo datos...")
    df = pd.read_csv(path)
    logger.info(f"Datos cargados correctamente. Filas: {len(df)}")
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Iniciando transformación de datos...")

    required_columns = ["Hours_Studied", "Attendance"]
    missing_cols = [col for col in required_columns if col not in df.columns]

    if missing_cols:
        raise ValueError(f"Faltan columnas obligatorias: {missing_cols}")

    df = df.drop_duplicates()
    df = df.dropna(subset=required_columns)

    df["Hours_Studied"] = pd.to_numeric(df["Hours_Studied"], errors="coerce")
    df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")

    df = df.dropna(subset=required_columns)
    df["Study_Effort"] = df["Hours_Studied"] * df["Attendance"]

    logger.info(f"Transformación completada. Filas finales: {len(df)}")
    return df


def load_data(df: pd.DataFrame, db_path: Path) -> None:
    logger.info("Cargando datos en SQLite...")

    conn = sqlite3.connect(db_path)
    df.to_sql("performance", conn, if_exists="replace", index=False)
    conn.close()

    logger.info(f"Datos cargados correctamente en {db_path}")


def pipeline(path: Path):
    df_raw = extract_data(path)
    df_clean = transform_data(df_raw)
    load_data(df_clean, DB_PATH)
    return df_clean


if __name__ == "__main__":
    df_final = pipeline(DATA_PATH)
    print(df_final.head())
