# ruta relativa
#open = sirve para abrir un archivo, si el archivo no existe se crea, la direccion de archivo va primero y se divide con el archivo con "/"
#"w"= significa el tipo de archivo que vamos a utilizar en este caso significa un archivo de escritura 
# archivo_abierto = open("carpeta/prueba.txt", "w")
# # weite= sirve para meter un texto dentro de un archivvo
# archivo_abierto.write("escribiendo la primera linea")
# archivo_abierto.close()
# #/n= sirve para dar una bajada de linea



# v 1 ejercicion cesar

# hobbie_archivo= open("prueba.txt", "w")
# variable= 1
# while variable != 4:
#      hobbie=input(f"cual es tu hobbie favorito:{variable} " )
#      print(hobbie)
#      variable += 1
#      hobbie_archivo.write(hobbie + "\n" )
# print(" gracias por ingresar tus tres hobbies ")
# hobbie_archivo.close()



#v2 profesor 
# archivo = open('miHobbieFavorito.txt', 'w')
# for numero in range(1, 4):
#     archivo.write(input(f'Ingrese su hobbie numero {numero}: ') + '\n')
# archivo.close()

# v3 con with. El with sirve para poder guardar un archivo en una variable 

# with open('texto.txt', 'w') as archivo_abierto:
#     # Trabajamos con el archivo
# # Una vez fuera del with el archivo se cierra solo

# with open('miHobbieFavorito.txt', 'w') as archivo:
#     for numero in range(1, 4):
#         archivo.write(input(f'Ingrese su hobbie numero {numero}: ') + '\n')
# print('Aca ya estamos por fuera del with')

#read= sirve para leer el archivo y tabn para convertilo en un string
# archivo= open ("prueba.txt" , "r")
# # print(archivo.read())
# archivo_lectura= archivo.read()
# print( archivo_lectura)
# archivo.close()
# print( archivo_lectura)

#readline= sirve para leer un archivo pero solo una linea del archivo

# archivo= open ("prueba.txt" , "r")
# print(archivo.readline())

# archivo = open('prueba.txt.txt', 'r')
# linea1_del_archivo = archivo.readline()
# print(linea1_del_archivo)
# linea2_del_archivo = archivo.readline()
# print(linea2_del_archivo)
# linea3_del_archivo = archivo.readline()
# print(linea3_del_archivo)
# archivo.close()

#readlines= devuelve todo el archivo pero te devuelve una lista de todas las lineas del archivo
#seek= sirve para leer el archivo desde la posicion que uno le indica
mi_dic= {
    "clave1": 1,
    "clave2": 2,
}
#json= para utilizar un archivo primero se usa la palabra import y deps json

import json
# with open("test.json", "w") as nuevo:
#     print(nuevo)
#     json.dump(mi_dic, nuevo, indent= 4)
    
#dump =sirve para guardar algo en un archivo json
# indent=sirve para crear identaciones
with open("test.json", "w") as nuevo:
    datos= json.load(nuevo)
    print( nuevo)
    print(type(nuevo))