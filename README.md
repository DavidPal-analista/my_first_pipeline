# Mini ETL Project – Student Performance

Este proyecto implementa un **pipeline ETL** simple en Python para procesar datos de desempeño estudiantil.  
El objetivo es extraer, limpiar y transformar un dataset CSV, y luego cargarlo en una base de datos SQLite.

---

## 📂 Estructura del proyecto

---

## ⚙️ Tecnologías

- Python 3.x  
- Pandas  
- SQLite3  
- Pathlib  
- Logging (para seguimiento de ejecución)

---

## 🚀 Flujo del pipeline

1. **Extract**: carga del dataset CSV desde la carpeta `data/`.  
2. **Transform**:  
   - Eliminación de duplicados y manejo de nulos.  
   - Conversión de tipos de columnas críticas (`Hours_Studied`, `Attendance`).  
   - Creación de columna derivada `Study_Effort` = `Hours_Studied * Attendance`.  
3. **Load**: guardado del dataframe limpio en una base de datos SQLite (`students.db`) en la tabla `performance`.  

---

## 💻 Cómo ejecutar

1. Clona el repositorio:  

```bash
git clone <URL-del-repo>
cd student_etl
