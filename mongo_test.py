from pymongo import MongoClient
from estudiante import Estudiante

#Crear conexion
cliente = MongoClient()

print(f'cliente: {cliente}')

#Crear base de datos
mongo_test = cliente.mongo_test
print(f'Mongo_test: {mongo_test}')

#Crear Colección
estudiantes = mongo_test.estudiantes

#Objeto diccionario

estudiante = {}
estudiante['nombre'] = 'Octavio'
estudiante['correo'] = '20111430@tecguanajuato.edu.mx'
estudiante['clases'] = ['Matematicas', 'Espaniol', 'Historia', 'Geografia']
result = estudiantes.insert_one(estudiante)
print(f'Insert ID: {result.inserted_id}')

#for i in estudiantes.find():
 #   print(i)

print(estudiantes.find({'nombre': 'Octavio'}))