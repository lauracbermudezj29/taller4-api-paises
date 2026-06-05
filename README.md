 
# Taller 4 - APIs Públicas, MongoDB y EDA

## Descripción

Proyecto desarrollado para la asignatura Bases de Datos para Ciencia de Datos.

Se utilizaró la API REST Countries para obtener información de países, almacenar los datos crudos en MongoDB y realizar un Análisis Exploratorio de Datos (EDA) mediante Python y Jupyter Notebook.

## API Utilizada

REST Countries API

https://restcountries.com/

## Tecnologías

- Python 3
- MongoDB
- Requests
- PyMongo
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Estructura del Proyecto

```text
├── ingesta.py
├── analisis.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar el script de ingesta:

```bash
python ingesta.py
```

## Base de Datos

- Base de datos: `taller4_db`
- Colección: `raw_data`

## Proceso Realizado

1. Extracción de datos desde la API REST Countries.
2. Almacenamiento de los datos sin modificaciones en MongoDB.
3. Lectura de los datos desde MongoDB.
4. Selección y limpieza de variables relevantes.
5. Análisis exploratorio de datos (EDA).
6. Generación de estadísticas descriptivas y visualizaciones.

## Análisis

El notebook `analisis.ipynb` contiene:

- Selección de variables.
- Limpieza de datos.
- Estadísticas descriptivas.
- 5 insights relevantes.
- 3 visualizaciones (incluyendo gráfico de torta).

## Autor

Laura Bermúdez
Universidad de Antioquia
