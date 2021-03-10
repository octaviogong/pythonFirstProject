from mongoengine import *
import datetime
from pprint import pprint


connect('IECA',host='localhost', port=27017)

#Modelo
class Post(Document):
    _nombre = StringField(required=True, max_length=200)
    _correo = StringField(required=True, max_length=50)
    _contrasena = StringField(required=True, max_length=50)
    _materias = ListField(StringField(required=True,max_length=20))
    _published = DateField(default=datetime.datetime.now(None))

print('Ingreso de estudiantes a base de datos IECA\n')
print('1.- Agregar estudiante')
print('2.- Mostrar estudiantes')
print('3.- Actualizar estudiantes')
print('4.- Eliminar estudiante')
print('5.- Salir\n')
select = int(input("Seleccion: "))




if __name__ == '__main__':

    while select < 5: #Crear objetos con ID nuevo en DB


        if select==1:

            post = Post(
                _nombre='',
                _correo='',
                _contrasena='',
                _materias=['']
                 )
            post._nombre = input('Ingresa un nombre: ')
            post._correo = input('Ingresa correo: ')
            post._contrasena = input('Ingresa contraseña: ')
            input_string = input("Ingresa materias separadas por coma: ")
            materias_lista = input_string.split(",")
            post._materias = materias_lista
            post.save()

            select = int(input("Seleccion: "))

        elif select == 2:

            for p in Post.objects:
                pprint(p._nombre)
                pprint(p._correo)
                pprint(p._materias)

            select = int(input("Seleccion: "))

        # [PV] Falta la implementacion de Actualizar y Eliminar
        elif select == 3:
            pass

