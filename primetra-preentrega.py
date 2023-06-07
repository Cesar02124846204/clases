
def registro(base_de_datos):
    nombre=input("ingresa el nuevo nombre del usario: " )
    contraseña=input("ingrese la nueva contraseña: ")
    usuario_nvo= {
        "nombre": nombre,
        "clave": contraseña,
    }
    base_de_datos.append(usuario_nvo)

    
def mostrar_usario(base_de_datos):
    for usario in base_de_datos:
        print( usario["nombre"])


def login(base_de_datos):
    existe_usario= False
    while not existe_usario :
        print("ingresa usario y contrasena")
        confirma_nombre=input("nombre de usario: ")
        confirmar_clave=input("contraseña del usario: ")
        
        for usario in base_de_datos:
            if usario["clave"] == confirmar_clave and  usario["nombre"] == confirma_nombre:
                print("existe el usuario")
                existe_usario= True
                break       

termina= False    
base_de_datos=[]

while not termina :
    opcion1= '1.-registro'   
    opcion2="2.-mostrar usario"
    opcion3="3.-login"
    opcion4= "4.-salir"
    
    print( opcion1, opcion2, opcion3,opcion4, sep="\n")
    opciones=input("que opcion quieres utilizar:  ")
    if "1" == opciones:
        registro(base_de_datos)

    elif "2" == opciones:
        mostrar_usario(base_de_datos)
    
    elif "3" ==opciones:
        login(base_de_datos)
        
    elif "4" == opciones:
        termina= True
        
    

# leer_data(base_de_datos)
    
    
    
# def login():
#     ...
