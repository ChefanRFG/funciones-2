lista=[]
def empezarlista():
    for _ in range(50):
        item=input("ingrese algo que quiera agregar, para terminar escriba fin: ")
        if item=="fin":
            print("cerrando la lista de compras...")
            break
        else:
            lista.append(item)

empezarlista()

def agregar():
    item=input("ingrese lo que quiere agregar: ")
    lista.append(item)

def remover():
    item=input("¿Qué objeto desea eliminar de la lista?: ")
    lista.remove(item)

while True:
    print("Seleccione lo que quiere hacer:")
    print("1. Agregar algo")
    print("2. Remover algo")
    print("3. Salir")
    opcion=input("Ingrese el número de la opción: ")

    if opcion == '1':
            agregar()
    elif opcion == '2':
            remover()
    elif opcion == '3':
            print("cerrando el programa...")
            break
    else:
            print("Opción no válida")
print(lista)