
from itertools import product
from flask import Flask, jsonify, request
import json
from functions import productos, limiteProducto

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    #Recibimos los datos desde el body, y aqui se convierte a un json 
    nombre = json.loads(request.data)
    if 'limite' not in nombre:
        #En este caso el ["productos"] lo que hace es retornar el valor asociado a la clave del diccionario
        titulos, urls, precios = productos(nombre['productos'])
    else:
        titulos, urls, precios = limiteProducto(nombre['productos'], nombre['limite'])
        
    return jsonify({"datos":{"titulos":titulos, "urls":urls, "precios":precios}})


if __name__ =="__main__":
    app.run()