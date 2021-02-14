def juego( opcion_jugador ,opcion_maquina): #Declaracion de la funcion del juego
 print('Máquina: ',opcion_maquina) #Se imprime la opcion aleatoria seleccionada por la maquina

 if(opcion_jugador==1 and opcion_maquina==3)or(opcion_jugador==2 and opcion_maquina==1)or(opcion_jugador==3 and opcion_maquina==2): #Condicion en las que el usuario podra ganar
     print("¡Ganaste!")
 elif opcion_jugador==opcion_maquina: #Condicion en la que se empata el juego
    print("¡Empate!")
 else:
     print("¡Perdiste! :(") #Todos los demás escenarios se imprime que el usuario pierde

