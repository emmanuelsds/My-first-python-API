from flask import Flask #, jsonify, request
#from pymongo import MongoClient

app = Flask(__name__)
#API's se pueden programar en todos los lenguajes
#
#Todos los endpoints son funciones
#swapi.dev
#coingecko.com/api/                                        https://api.coingecko.com/api/v3/

@app.route('/')#Decorador -> Darle poderes extra a una función: @nombredeldecorador)
def root():
    print('Hola')


#Levantar el servidor de nuesra web App
#localhost = 127.0.0.1
#port = 3306 MySQL, 80 FTP, 8080, etc...
app.run(debug=True, host='localhost', port=5000)