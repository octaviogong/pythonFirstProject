from Tarea2_Funcion import validar_correo
from Tarea2_Funcion import validar_telefono
from Tarea2_Funcion import validar_rfc
from Tarea2_Funcion import validar_curp

print('Ingresa tu correo electrónico') #Mensaje de bienvenida al usuario

correo_electronico= input('Correo: ') #El usuario intoduce su correo electrónico
validar_correo(correo_electronico)  #Se valida correo electronico

print('Ingresa tu teléfono')

telefono_usuario= input('Teléfono: ') #El usuario intoduce su teléfono
validar_telefono(telefono_usuario)  #Se valida telefono

print('Ingresa tu RFC')

rfc_usuario= input('RFC: ') #El usuario intoduce su RFC
validar_rfc(rfc_usuario)  #Función que valida RFC

print('Ingresa tu CURP')

curp_usuario= input('CURP: ') #El usuario intoduce su CURP
validar_curp(curp_usuario)  #Función que valida CURP