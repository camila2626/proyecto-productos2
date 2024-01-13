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
    origen= input("origen:" )
    descripcion = input("descripcion: ")
    disponible = input("esta disponible? ")
    categoria = input("elegi una categoria para el producto: ")
    producto = {"codigo": codigo, "descripcion": descripcion, "disponible": disponible, "categoria": categoria, "origen": origen}
    listado.append(producto)
    print(producto)
    grabarArchivo(listado)


def modificarProducto(listado):
    print()
    buscarPorCodigo = int(input("codigo de producto a modificar: "))
    for producto in listado:
        if buscarPorCodigo == producto["codigo"]:
            nuevoCodigo = input(
                f"{producto['codigo']} ingresa el nuevo codigo (si ingresas 0 no se modifica): "
            )
            nuevaDescricion = input(
                f"{producto['descripcion']} Ingresa nueva descripcion (si ingresa 0 no se modifica): "
            )
            nuevaCategoria = input(
                f"{producto['categoria']} Ingrese la nueva categoria (si ingresa 0 no se modifica): "
            )
            nuevoOrigen = input(
                f"{producto['origen']} Ingrese el nuev origen (si ingresa 0 no se modifica): "
            )
            if nuevaDescricion != "0" and nuevaDescricion != "":
                producto["descripcion"] = nuevaDescricion

            if nuevoCodigo != "0" and nuevoCodigo != "":
                producto["codigo"] = int(nuevoCodigo)
            
            if nuevaCategoria!= "0" and nuevaCategoria!= "":
                producto["categoria"] = nuevaCategoria

            if nuevoOrigen!= "0" and nuevoOrigen!= "":
                producto["origen"] = nuevoOrigen

            grabarArchivo(listado)
            break
        
def eliminarProducto(listado):
    codigoAbuscar = int(input("ingresa el codigo del producto a eliminar: "))
    for producto in listado:
        if codigoAbuscar == producto["codigo"]:
            listado.remove(producto)
            grabarArchivo(listado)
            break


def mostrarTodos(listado):
    print(listado)

def mostrarPruebas(productos):
    print(productos)

def leerProductos():
    archivo = open("productos.json")
    listado = json.load(archivo)
    archivo.close()
    return listado

def categorizar(listado):
    print("que cateroria va a asignar?") 
    categoria_del_producto = input("ingrese la categoria: ")
    while True:
       codigo_producto = input("codigo del producto que va a cambiar su categoria: ")
       if codigo_producto == "":
           break
       codigo_producto = int(codigo_producto)
       encontrado = False
       for producto in listado:
        if codigo_producto == producto["codigo"]:
            producto["categoria"] = categoria_del_producto
            print(f"se actualizo la categoria del producto {producto['descripcion']}"  )
            grabarArchivo(listado)
            encontrado = True
            break
       if encontrado == False:
           print("no se encontro el codigo ")


# aca empieza el programa
productos = leerProductos()
while True:
    print(
        f"""
         1- Alta de producto
         2- Modificacar producto
         3- Eliminar producto
         4- Mostrar todos los productos
         5- categorizar
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
        categorizar(productos)
    
    elif opcion == "0":
        break
