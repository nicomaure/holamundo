# Mi Primera Web (Hola Mundo)

Este es mi primer proyecto de desarrollo web creado con Python. Es una aplicación simple que muestra el mensaje "¡Hola, Mundo!" en un navegador.

El objetivo de este proyecto fue aprender los fundamentos de:
- Configuración de un entorno de desarrollo con PyCharm.
- Uso de entornos virtuales (`venv`).
- Creación de una aplicación básica con el framework Flask.
- El flujo de trabajo completo de Git y GitHub (commit, push, etc.).

## Tecnologías Utilizadas
- Python 3
- Flask

## Cómo Ejecutarlo Localmente

Si quieres probar este proyecto en tu propia computadora, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/nicomaure/holamundo.git](https://github.com/nicomaure/holamundo.git)
    ```
2.  **Navegar a la carpeta del proyecto:**
    ```bash
    cd holamundo
    ```
3.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows es `venv\Scripts\activate`
    ```
4.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Ejecutar la aplicación:**
    ```bash
    python app.py
    ```
6.  Abre tu navegador y ve a `http://127.0.0.1:5000`.