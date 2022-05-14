Trabajo semanal 1

Requisitos:
    
- Python 3.x

Pasos para la ejecución del programa

1. Descromprimir el codigo fuente de la aplicacion

2. Ingresar a la ruta donde se encuentra el codigo descomprimido

3. Crear un entorno virtual para trabajar con las librerias correspondientes
    python -m venv venv

4. Ingresar al entorno virtual previamente creado
    .\venv\Scripts\activate

5. Instalar las librerias que se utilizan en el proyecto
    pip install -r requirements.txt

6. Ejecutar el programa
    python app.py

7. Seleccionar la imagen, estilo, ruido y X2 desde la interfaz gráfica, posibles valores:
    ruido 1 - x2 1
    ruido 2 - x2 2

8. Presionar el botón de convertir imagen desde la interfaz gráfica

9. En la raiz del proyecto se creo un archivo 'resultado.jpg' con el resultado de la api.

Para salir del entorno virtual se ejecuta el siguiente comando
    .\venv\Scripts\deactivate