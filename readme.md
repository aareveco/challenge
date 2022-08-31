# Challenge


## Setup
Python >=3.8 \
Instalar requirements.txt \
[Descargar el archivo de muertes por causas](https://data.cdc.gov/NCHS/Monthly-Counts-of-Deaths-by-Select-Causes-2014-201/bxq8-mugm)
## Files
* El archivo __constants.py__ contiene las constantes usadas en el resto de los archivos
* El archivo __create_tables.py__ crea el esquema de las tablas y genera un archivo .sqlite con el nombre asociado a DB_NAME en el archivo constants.py
* El archivo __populate_tables.py__ consume el archivo de muertes .csv y agrega la info a las tablas correspondientes
* El archivo __query_tables.py__ contiene las consultas al modelo de datos

## Usage
Si no existe el archivo .sqlite en la ruta de la carpeta  se puede crear ejecutando el siguiente comando
```cmd
python create_tables.py
```
En caso de existir arrojará error dado que las tablas que se intentan crear ya existen. \
Para poblar las tablas utilizar el siguiente comando:
```cmd
python populate_tables.py
```
Si las Tablas ya están pobladas arrojará error por intentar insertar datos duplicados.
python

Finalmente para las respuestas a las preguntas ejecutar:
```cmd
python query_tables.py
```
## Notes

Asumí que las causas 'All Cause' y 'Natural Cause' del set de datos englobaban múltiples causas y que en teoría todas las causas por separadas debían sumar el valor de 'All Cause' para cada mes-año, sin embargo no encontré dicha combinación ni la explicación del set de datos por lo que conserve ambas categorías, pero asumí que cuando se pregunta las mayores causas de muerte se pretendía dejar estas causas fuera, por lo que en las consultas dentro de __query_tables.py__ hay líneas comentadas en caso de que este supuesto este incorrecto.