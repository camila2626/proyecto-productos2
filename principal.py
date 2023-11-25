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
    producto = {"codigo": codigo, "descripcion": descripcion}
    listado.append(producto)
    print(producto)
    grabarArchivo(listado)


def modificarProducto(listado):
    print()
    buscarPorCodigo = int(input("codigo de producto a modificar: "))
    for producto in listado:
        if buscarPorCodigo == producto["codigo"]:
            nuevaDescricion = input(
                f"{producto['descripcion']} Ingresa nueva descripcion (ingresa 0 para no modificar):"
            )
            if nuevaDescricion != "0":
                producto["descripcion"] = nuevaDescricion
            if buscarPorCodigo != "0":
                producto["codigo"] = buscarPorCodigo

            grabarArchivo(listado)
            break


def eliminarProducto(listado):
    codigoAbuscar = int(input("codigo del producto a eliminar:"))
    for producto in listado:
        if codigoAbuscar == producto["codigo"]:
            archivo = open("productos.json")
            json.dump(listado, archivo, indent=2)
            archivo.close()
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
         0- Salir
         """
    )
    opcion = input("Opcion: ")
    #opcion = int(opcion)

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
