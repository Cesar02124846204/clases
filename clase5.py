# bandera o flag= cuando una variable es verdadera y se puede transformar en falsa dentro de un while

# repetir_menu = True # bandera/flag
# while repetir_menu:
#     print('''
#     ==============
#     ==============
#     1. Retirar efectivo.
#     2. Cambiar contraseña.
#     3. Salir
#  ''')
#     opcion_elegida = input('Ingrese la operacion a realizar: ')
#     if opcion_elegida == '1':
#         print('Retiro efectivo.')
#     elif opcion_elegida == '2':
#          print('Cambio la contraseña.')
#     elif opcion_elegida == '3':
#          repetir_menu = False
#          print('Hasta luego!')
#     else:
#          print('Vuelva a intentar con una opcion valida.')
numeros=[1,5,4,324,2,42,4,24,2432]
valor_extraido= 0
while valor_extraido != 5:
    valor_extraido= numeros.pop()
    print(valor_extraido)
