# flow by 0miKron
### Un programa para apoyar a todo aquel en búsqueda de buena y especializada rima en español.

## Separación Silábica - Spanish Syllabic Separation - `silabas.py`
El algoritmo Open Source de separación silábica disponible en el repositiorio principal de este proyecto está listo para ser implementado dentro de cualquier programa en Python de análisis lírico. Contiene los siguientes atributos: 
- **Separación Silábica** con todas las consideraciones de la lengua española, eje principal del análisis métrico.
- **Sílaba Tónica** encuentra el índice de la sílaba tónica para futura referencia una vez encontrada la separación silábica. 
- **Categoría de Palabras** con la información de `s_silabas()` y `s_tonicas()`se consiguen el típo de palabra que se analiza. 
- **Fonemas Consonantes** los fonemas que contiene cualquier otra palabra que haga rima consonante con la palabra.
- **Fonemas Asonantes** los fonemas que contiene cualquier otra palabra que hagan rima asonante con la palabra. 

## flow - Programa
Una aplicación de terminal Open Source Offline escrita en Python para que el usuario encuentre de manera rápida y específica rimas, agregue nuevo vocabulario, ya sea a partir de textos completos o por palabras específicas, y quite palabras a su elección.
Todos los datos de la aplicación de encuentran [aquí](https://github.com/0kron/flow/tree/main/flow) para su revisión. 

### Para usuarios de Linux: 
Se puede instalar de manera rápida el proyecto de la manera: 

`git clone https://github.com/0kron/flow/tree/main/flow`

Y haciendo un `cd flow/` se puede correr el módulo main(): 

`python3 main.py`

### Para usuarios de Windows: 
Copiar la carpeta de **flow** dentro de su ruta de preferencia, asegurarse de que python3 está instalado con: 

`python3 -V` 

Y correr el archivo desde terminal. 

**Nota:** Es importante revisar los comandos del módulo file_reader.py, debido a que las rutas de acceso para ambos archivos *.txt* no están especificadas, añadido esto a que el comando para añadir vocabulario a partir de un texto emplea *gedit* pero este puede ser cambiado por editores de text como *vim*, *nano*, *notebook*, etc. 

**El programa está abierto a comentarios sobre eficiencia, velocidad o nuevas acciones* 

