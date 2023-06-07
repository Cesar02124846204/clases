# conjuntos o set
# lista= ["uno","dos","3","4"]
# tupla= ("1","tres","dos")
# conjuntos={"hola","mentira", "verdad",True}
#los set o conjuntos estas optimizados para realizar los tipos de operaciones matematicas

# otros_datos = []
# otros_datos1 = ()
# otros_datos2 = {}
# otros_datos3 = set()
# print(type(otros_datos))
# print(type(otros_datos1))
# print(type(otros_datos2))
# print(type(otros_datos3))

# los set son mutables pero no se pueden buscar los datos internamente porque se guardan de forma aleatorea
# los set no pueden guardar datos que sean mutables

#los set nos preveen de elementos repetidos



# #metodo add= sirve para agregar un dato a un set
# auto = {'v8', 'Negro', (6, 'blindadas')}
# # lista = [1, 2, 3, 'probando']
# tupla = (1, 2, 3, 'probando')
# auto.add('descapotable')
# # auto.add(lista)
# auto.add(tupla)
# print(auto)
# metodo update= sirve para agragar varios valores
# lista = ['soy', 'una', 'lista']
# tupla = ('soy', 'una', 'tupla')
# cadena = 'soy una cadena'
# rango = range(15)
# auto.update(lista)
# print(auto)
# auto.update(tupla)
# print(auto)
# auto.add(cadena)
# auto.update(cadena)
# print(auto)
# auto.update(rango)
# print(auto)

#funcion len= siver para saber la cantidad de elementos que tiene un set
# print(len(auto))


#metodo discard= sirve para eliminar elementos de un set, hay que decirle el elemento exacto que queremos extraer
# auto = {'v8', 'Negro', (6, 'blindadas')}
# auto.discard('lista')
# print(auto)
# auto.add('lista')
# print(auto)
# auto.discard('lista')
# print(auto)


# Método remove ( discard pero con generacion de error )

# auto = {'v8', 'Negro', (6, 'blindadas')}
# auto.remove('tupla')
# print(auto)
# auto.add('tupla')
# print(auto)
# auto.discard('tupla')
# print(auto)

#in= funcioma para determinar si algun valor esta dentro de la variable ej: "pedro" in auto osea "pedro" se encuentra adentro de auto
#not in= para verificar que un elemento no esta en la lista
# auto = {'v8', 'Negro', (6, 'blindadas')}
# for dato in auto:
#     print(dato)
# print('descapotable' in auto)
# print('caño de escape' not in auto)
# lista = [1,2,3,4]
# print(1 in lista)

#clear = sirve para limpiar un set "set.clear()"


#pop= va sacando un elemento primer elemento  del set
# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(auto)
# valor = auto.pop()
# print(auto)
# print(valor)


#diccionarios = se continen en una llave al igual que un conjunto pero se organizan de forma distinta
# diccionario= {
#     1: hola,
#     2: comoestas,
#     3: bien
#     }

#  auto = {'v8', 'Negro', (6, 'blindados')}
#  print(auto)
#  motor = 'v8'
#  color = 'Negro'
# el diccionario es un tipo de dato mutable
auto = {
    'motor': 'v8',
    "color": 'Negro',
    'vidrios': (6, 'blindados'),
    'pasajeros': 4,
}
print(auto)
print(auto['motor'])
print(auto.get("color"))