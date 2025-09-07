# Importamos la clase Flask desde la librería que instalamos
from flask import Flask

# 1. Creamos una instancia de la aplicación
app = Flask(__name__)

# 2. Definimos una "ruta" y la función que se ejecutará
@app.route('/')
def hola_mundo():
    """
    Esta función se ejecuta cuando alguien visita la página principal.
    """
    return '¡Hola, Mundo desde mi primera aplicación web!'

# 3. Ponemos en marcha el servidor de desarrollo# Importamos la clase Flask desde la librería que instalamos
# from flask import Flask
#
# # 1. Creamos una instancia de la aplicación
# app = Flask(__name__)
#
# # 2. Definimos una "ruta" y la función que se ejecutará
# @app.route('/')
# def hola_mundo():
#     """
#     Esta función se ejecuta cuando alguien visita la página principal.
#     """
#     return '¡Hola, Mundo desde mi primera aplicación web!'
#
# # 3. Ponemos en marcha el servidor de desarrollo
# if __name__ == '__main__':
#     # debug=True hace que el servidor se reinicie automáticamente cuando haces cambios
#     # y muestra errores más detallados en el navegador.
#     app.run(debug=True)
if __name__ == '__main__':
    # debug=True hace que el servidor se reinicie automáticamente cuando haces cambios
    # y muestra errores más detallados en el navegador.
    app.run(debug=True)