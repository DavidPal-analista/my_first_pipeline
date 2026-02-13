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


# Mini Data Warehouse: Student Performance Factors

## 🔹 Descripción del proyecto

Este proyecto es un **mini Data Warehouse** construido a partir de un dataset de factores que influyen en el rendimiento de estudiantes.  
El objetivo es **demostrar un pipeline completo de Data Engineering**, incluyendo:

1. **ETL básico**: carga, limpieza y transformación del CSV.  
2. **Dimensiones**: creación de tablas de dimensiones (`DimStudent`, `DimSchool`, `DimActivity`).  
3. **Fact Table**: tabla de hechos (`FactPerformance`) con métricas como `Hours_Studied`, `Attendance`, `Study_Effort` y `Exam_Score`.  
4. **Almacenamiento en SQLite** para consultas SQL.

---

## 🔹 Estructura de archivos

pipeline/
│
├── data/
│ └── StudentPerformanceFactors.csv
│
├── pipeline_sencillo.py
└── README.md



- `data/StudentPerformanceFactors.csv`: dataset original.  
- `pipeline_sencillo.py`: script que crea el mini Data Warehouse.  
- `students_dw.db`: base de datos SQLite generada al ejecutar el script.

---

## 🔹 Star Schema

**Dimensiones:**

- **DimStudent**: Género, Educación de los padres, Ingresos familiares  
- **DimSchool**: Tipo de escuela, Calidad del profesor  
- **DimActivity**: Actividades extracurriculares y físicas  

**Fact Table:**

- **FactPerformance**: Horas estudiadas, Asistencia, Esfuerzo (`Study_Effort`), Nota de examen  
- Claves foráneas: `student_id`, `school_id`, `activity_id`  


    DimStudent      DimSchool     DimActivity
      |                |              |
      +----------------+--------------+
                       |
                 FactPerformance
