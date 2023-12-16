import json
import os

d = os.path.dirname(__file__)
os.chdir(d)
productos = []


def grabarArchivo(listado):
    archivo = open("productos.json", "w")
    json.dump(listado, archivo, indent=2)
    archivo.close()


def altaDeProducto(listado):
    codigo = int(input("codigo:"))
    descripcion = input("descripcion: ")
    disponible = input("esta disponible? ")
    categoria = input("elegi una categoria para el producto: ")
    producto = {"codigo": codigo, "descripcion": descripcion, "disponible": disponible, "categoria": categoria}
    listado.append(producto)
    print(producto)
    grabarArchivo(listado)


def modificarProducto(listado):
    print()
    buscarPorCodigo = int(input("codigo de producto a modificar: "))
    for producto in listado:
        if buscarPorCodigo == producto["codigo"]:
            nuevoCodigo = input(
                f"{producto['codigo']} ingresa el nuevo codigo (ingresa 0 para no modificar): "
            )
            nuevaDescricion = input(
                f"{producto['descripcion']} Ingresa nueva descripcion (ingresa 0 para no modificar): "
            )
            if nuevaDescricion != "0" and nuevaDescricion != "":
                producto["descripcion"] = nuevaDescricion

            if nuevoCodigo != "0" and nuevoCodigo != "":
                producto["codigo"] = int(nuevoCodigo)

            grabarArchivo(listado)
            break
        
def eliminarProducto(listado):
    codigoAbuscar = int(input("codigo del producto a eliminar:"))
    for producto in listado:
        if codigoAbuscar == producto["codigo"]:
            listado.remove(producto)
            grabarArchivo(listado)
            break


def mostrarTodos(listado):
    print(listado)


def leerProductos():
    archivo = open("productos.json")
    listado = json.load(archivo)
    archivo.close()
    return listado

    


# aca empieza el programa
productos = leerProductos()
while True:
    print(
        f"""
         1- Alta de producto
         2- Modificacar producto
         3- Eliminar producto
         4- Mostrar todos los productos
         5- mostrar pruebas
         6- categorizar
         0- Salir
         """
    )
    opcion = input("Opcion: ")
    # opcion = int(opcion)

    if opcion == "1":
        altaDeProducto(productos)
    elif opcion == "2":
        modificarProducto(productos)
    elif opcion == "3":
        eliminarProducto(productos)
    elif opcion == "4":
        mostrarTodos(productos)
    elif opcion == "5":
        print("pruebas")
    
    elif opcion == "0":
        break
