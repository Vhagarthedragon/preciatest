# PRECIA Dev test
## Preguntas a responder
###  2.	¿Cuáles son las diferencias entre los tipos de datos CHAR y VARCHAR? *
- CHAR: cadenas de longitud fija. Si la cadena es más corta que la longitud especificada, se completa con espacios en blanco.
- VARCHAR:  Almacena cadenas de longitud variable. Ocupa solo el espacio necesario para almacenar la cadena, sin espacios en blanco adicionales.


### 3.	¿Cuál es mejor tipo para almacenar un precio? *
- El más adecuado para almacenar precios es generalmente el tipo de dato `DECIMAL` o `NUMERIC`. son mas precisos y se utilizan para valores que requieren exactitud decimal, como los precios.

### 4.	Escriba un query MySQL que permita insertar la siguiente fecha ‘20220220‘ (2022-02-20) en la columna ’valuation date‘ de la siguiente tabla, por favor mantenga el formato original de la fecha.

     `CREATE TABLE us bussines days( vaIuation_date DATE NOT NULL, PRIMARY KEY(vaIuation_date));`

     `INSERT INTO us_bussines_days (valuation_date) VALUES ('2022-02-20');`



###  5.	¿Cuál puede ser la posible causa del siguiente mensaje de error: `“ERROR 1062 (23000): Duplicate entry 'EURUSD' for key 'PRIMARY"‘?`
- Este mensaje puede indicar que está intentando insertar o actualizar un registro en el que el valor de la columna que tiene la restricción de clave primaria ('PRIMARY') ya existe en otra fila. En este caso, 'EURUSD' está duplicado en la columna clave primaria. Puede deberse a intentos de insertar un valor que ya existe en la tabla o a problemas de sincronización en la base de datos. Para poder resolverlo, se puede eliminar o corregir los duplicados que ya esten.


### 6.	Defina en sus palabras que es una AWS lambda 
   - AWS Lambda es un servicio que permite ejecutar codigo en respuesta a eventos sin necesidad de aprovisionar o gestionar servidores. a esto se llama arquitectura serverless

### 7.	¿Como usar librerias Python no nativas en AWS lambda? 
   - Puedes incluir librerías Python no nativas en AWS Lambda empaquetándolas con docker y subiéndolas como un archivo ZIP en un s3, definiendo sus dependencias, al momento de desplegarse la imagen, se instalaran automaticamente en el enviroment

### 8.	Defina en sus palabras que es una AWS S3 bucket 
   - Un bucket de Amazon S3 (Simple Storage Service) es un contenedor de almacenamiento en la nube que permite almacenar y recuperar cualquier cantidad de datos en cualquier momento desde la web. Puedes almacenar una amplia variedad de tipos de datos, como archivos, imágenes, videos y conjuntos de datos.

### 9.	¿Que es el ciclo de vida de un AWS bucket S3? 
 - El ciclo de vida de un bucket de Amazon S3 se refiere a las etapas por las que pasa un objeto almacenado en el bucket, desde su creación hasta su eliminación. Incluye eventos como la creación, transiciones de almacenamiento, y expiración. se puede configurar políticas de ciclo de vida para automatizar acciones en objetos basadas en su antigüedad o cambios en su clase de almacenamiento.

### 10.	Defina en sus palabras que son los procesos ETL 
- Los procesos ETL son una serie de pasos utilizados para la extracción, transformación y carga de datos de una fuente a un destino. 
      - **Extract (Extracción):** Obtener datos de una o varias fuentes.
      - **Transform (Transformación):** Modificar y dar formato a los datos para que sean adecuados para el análisis.
      - **Load (Carga):** Insertar los datos transformados en un almacén de datos o destino.

### 11. ¿Cual es el servicio AWS por excelencia para desplegar procesos ETL? 
- AWS Glue es el servicio de AWS diseñado específicamente para realizar procesos ETL. Facilita la preparación y carga de datos para su análisis, permitiendo descubrir, transformar y mover datos de manera eficiente entre almacenes de datos. Utiliza un enfoque serverless y escalable, gestionando la complejidad del entorno de ejecución de ETL.
