import re #Libreria para expresiones regulares

def validar_correo(correo): #Declaracion de la funcion que validará correo

#Expresion regular para correos tipo Ej. juan.valenzuela@curso.python.mx
    # [PV] Da como error con el correo: juan@cinvestav.mx
    # expresion_regular_correo= r'[\w-]{1,20}\.[\w-]{1,20}@\w{2,5}\.\w{2,6}\.\w{1,2}$'

    # [PV] Sugerencia
    expresion_regular_correo= r'([\w-]{1,20}\.)?[\w-]{1,20}@(\)w{2,5}\.)?\w{3,15}\.\w{1,2}$'


    if re.match(expresion_regular_correo, correo) is not None:
       print('Correo VALIDO')
    else:
        print('Correo INVALIDO')

def validar_telefono(telefono): #Declaracion de la función que validará teléfono

#Expresiones regulares para numeros telefónicos
  expresion_regular_tel1= r'[0-9]{10}$'
  expresion_regular_tel2= r'\([0-9]{2}\)[0-9]{8}$'
  expresion_regular_tel3= r'\([0-9]{3}\)[0-9]{7}$'
  expresion_regular_tel4= r'\([0-9]{2}\)\ [0-9]{4}\ [0-9]{4}$'
  expresion_regular_tel5= r'\([0-9]{3}\)\ [0-9]{3}\-[0-9]{4}$'

#Se valida la coincidencia con alguno de los formatos

  if  re.match(expresion_regular_tel1, telefono) is not None:
    print('Teléfono  VALIDO')
  elif re.match(expresion_regular_tel2, telefono) is not None:
    print('Teléfono  VALIDO')
  elif re.match(expresion_regular_tel3, telefono) is not None:
    print('Teléfono  VALIDO')
  elif re.match(expresion_regular_tel4, telefono) is not None:
    print('Teléfono  VALIDO')
  elif re.match(expresion_regular_tel5, telefono) is not None:
    print('Teléfono  VALIDO')
  else:
    print('Teléfono INVALIDO') #Cualquier otro formato es invalido

def validar_rfc(rfc): #Declaracion de la función que validará RFC
    #Expresion regular para validar rfc

    expresion_regular_rfc = r'[A-Z]{4}[0-9]{6}[A-Z0-9]{3}$'
#Comparación unica con la expresion regular

    if re.match(expresion_regular_rfc, rfc) is not None:
        print('RFC VALIDO')
    else:
       print('RFC INVALIDO') #Cualquier otro formato es invalido

def validar_curp(curp): #Declaracion de la función que validará CURP
    # Expresion regular para validar CURP

    expresion_regular_curp = r'[A-Z]{4}[0-9]{6}[HM]{1}[A-Z]{5}[0-9]{2}$'

    # Comparación unica con la expresion regular

    if re.match(expresion_regular_curp, curp) is not None:
        print('CURP VALIDO')
    else:
        print('CURP INVALIDO')  # Cualquier otro formato es invalido