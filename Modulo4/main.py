from gestor import GestorClientes
from errores import EmailInvalidoError


gestor = GestorClientes()

while True:
    print("\n--- GESTOR INTELIGENTE DE CLIENTES ---")
    print("1. Crear cliente")
    print("2. Mostrar clientes")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Guardar en CSV")
    print("6. Cargar desde CSV")
    print("7. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        email = input("Email: ")
        telefono = input("Telefono: ")
        direccion = input("Direccion: ")

        print("1. Regular")
        print("2. Premium")
        print("3. Corporativo")
        tipo = input("Tipo de cliente: ")

        try:
            gestor.agregar_cliente(nombre, email, telefono, direccion, tipo)
        except EmailInvalidoError as error:
            print("Error:", error)

    elif opcion == "2":
        gestor.mostrar_clientes()

    elif opcion == "3":
        email = input("Correo del cliente a editar: ")
        gestor.editar_cliente(email)

    elif opcion == "4":
        email = input("Correo del cliente a eliminar: ")
        gestor.eliminar_cliente(email)

    elif opcion == "5":
        gestor.guardar_csv()

    elif opcion == "6":
        gestor.cargar_csv()

    elif opcion == "7":
        print("Programa finalizado")
        break

    else:
        print("Opcion no valida")
