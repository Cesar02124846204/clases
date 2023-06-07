# #upper= copia la cadena y pone todos los elementos en mayuculas 
# # ejem
# cadena= "soY PriMera Cadena"
# print(cadena)
# cadena_de_prueba= cadena.upper()
# print(cadena_de_prueba)

# #lower= sirve para pasar a minuscula un string
# cadena2= "HOLA SOY LA SEGUNDA CADENA"
# print(cadena2)
# cadena2= cadena2.lower()
# print(cadena2)


# #capitalize= esta funcion es para pasar la primera letra del string a matuscula y dejar todas la demas en minuscula 
# cadena3="HOLA SOY LA TERCERA CADENA "
# print(cadena3)
# cadena3= cadena3.capitalize()
# print(cadena3)


# #title = pone el mayuscula todas las primeras letras de cada palabra
# cadena4= "soy la cuarta cadena "
# print(cadena4)
# cadena4= cadena4.title()
# print(cadena4)


# metodo cuont = siver para hacer busqueda de cualquier pedazo de string 
cadena1 = 'soY la pRimer cadena'
cadena1 = 'soY la pRimeroY cadenaoY  oY'
print(cadena1.count('oy'))
print(cadena1.count('oY'))
print(cadena1.count('a'))
print(cadena1.count('a', 2))
print(cadena1.count('a', 7))
print(cadena1.count('a', 2, 16))