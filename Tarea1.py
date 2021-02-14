from Tarea1_Funcion import juego #Llamar al modulo Tarea1_Funcion donde se evaluan las opciones
import random #libreria para funciones de tipo aleatorias


print('¡Jugaremos piedra, papel o tijera!') #Mensaje de bienvenida al usuario
print('Seleccione una opción:\n1.- Piedra\n2.- Papel\n3.- Tijera') #Opciones que podrá jugar el usuario

opcion= int(input('Opción: ')) #El usuario intoduce la opcion

juego(opcion, random.randint(1,3)) #Se manda a llamar la funcion juego del modulo Tarea1_Funcion


