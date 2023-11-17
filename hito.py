base_de_datos_clientes = {}
#hacemos un diccionario de los productos
productos = {
    1: {'nombre': 'Bolsas', 'precio': 10.99},
    2: {'nombre': 'FIFA 24', 'precio': 40.49},
    3: {'nombre': 'Cartera', 'precio': 5.99},
    4: {'nombre': 'Chocolatina', 'precio': 1.79},
    5: {'nombre': 'Alcatel', 'precio': 90.99},
    6: {'nombre': 'GTA V', 'precio': 29.99},
    7: {'nombre': 'Destornillador', 'precio': 9.49},
    8: {'nombre': 'Ratón', 'precio': 15.99},
    9: {'nombre': 'Teclado', 'precio': 30.99},
    10: {'nombre': 'Bebida energética', 'precio': 1},
    11: {'nombre': 'Baúl', 'precio': 9.99}
}
#Creamos la funcion registrar_cliente
def registrar_cliente():
    #printeamos un mensaje de bienvenida
    print("Bienvenido al proceso de registro.")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese una contraseña: ")


    id_cliente = len(base_de_datos_clientes) + 1

   #almacena los datos que le hemos proporcionado para luego facilitarle a los print el nombre, apellidos...
    base_de_datos_clientes[id_cliente] = {
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo,
        'contrasena': contrasena
    }
#una vez almacenados le damos un mensaje y le enviamos a lo que seria la pagina principal
    print("¡Perfecto!")
    pagina_principal(id_cliente)
#creamos la funcion enviar factura para 'simular' que se envia la factura al correo proporcionado
def enviar_factura(correo, productos_seleccionados, total):
    print("\nEnviando factura a:", correo)
    print("\nDetalle de la compra:")
    for producto in productos_seleccionados:
        print(f"{producto['nombre']} - {producto['precio']:.2f}€")
    print(f"Total: {total:.2f}€")

def pagina_principal(id_cliente):
    print(f"Bienvenido, {base_de_datos_clientes[id_cliente]['nombre']} {base_de_datos_clientes[id_cliente]['apellido']}!")
    print("\nCatálogo de productos:")
    for id_producto, producto_info in productos.items():
        print(f"{id_producto}. {producto_info['nombre']} - {producto_info['precio']:.2f}€")
    productos_seleccionados = []
    while True:
        seleccion = input("Ingrese el número del producto que desea comprar (o 'exit' para salir): ")
        if seleccion.lower() == 'exit':
            break
        try:
            id_producto = int(seleccion)
            if id_producto in productos:
                productos_seleccionados.append(productos[id_producto])
                print(f" '{productos[id_producto]['nombre']}' se ha añadido al carrito correctamente.")
            else:
                print("Número de producto inválido. Intente de nuevo.")
        except ValueError:
            print("No encontramos ese producto, vuelve a intentarlo.")
    print("\nResumen :")
    total = sum(producto['precio'] for producto in productos_seleccionados)
    for producto in productos_seleccionados:
        print(f"{producto['nombre']} - {producto['precio']:.2f}€")
    print(f"Total: {total:.2f}€")
    num_tarjeta = input("Ingrese el número de tarjeta: ")
    direccion_envio = input("Ingrese la dirección de envío: ")
    base_de_datos_clientes[id_cliente]['num_tarjeta'] = num_tarjeta
    base_de_datos_clientes[id_cliente]['direccion_envio'] = direccion_envio
    enviar_factura(base_de_datos_clientes[id_cliente]['correo'], productos_seleccionados, total)
    print("Muchas gracias por comprar en nuestra tienda, se le enviará una copia de la factura al correo seleccionado, vuelva pronto!!!")
registrar_cliente()




