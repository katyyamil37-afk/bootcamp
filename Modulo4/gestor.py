from cliente import ClienteRegular, ClientePremium, ClienteCorporativo
from errores import EmailInvalidoError


class GestorClientes:
    def __init__(self):
        self.clientes = []

    def validar_email(self, email):
        if "@" not in email:
            raise EmailInvalidoError("El correo debe contener @")

    def buscar_cliente(self, email):
        for cliente in self.clientes:
            if cliente.obtener_email() == email:
                return cliente
        return None

    def agregar_cliente(self, nombre, email, telefono, direccion, tipo):
        self.validar_email(email)

        if self.buscar_cliente(email) is not None:
            print("Ya existe un cliente con ese correo")
            return

        if tipo == "1":
            cliente = ClienteRegular(nombre, email, telefono, direccion)
        elif tipo == "2":
            cliente = ClientePremium(nombre, email, telefono, direccion)
        elif tipo == "3":
            cliente = ClienteCorporativo(nombre, email, telefono, direccion)
        else:
            print("Tipo de cliente no valido")
            return

        self.clientes.append(cliente)
        self.guardar_log("Cliente creado: " + email)
        print("Cliente agregado correctamente")

    def mostrar_clientes(self):
        if len(self.clientes) == 0:
            print("No hay clientes registrados")
        else:
            for cliente in self.clientes:
                print(cliente, "-", cliente.tipo_cliente())

    def editar_cliente(self, email):
        cliente = self.buscar_cliente(email)

        if cliente is None:
            print("Cliente no encontrado")
            return

        cliente.nombre = input("Nuevo nombre: ")
        cliente.telefono = input("Nuevo telefono: ")
        cliente.direccion = input("Nueva direccion: ")

        self.guardar_log("Cliente editado: " + email)
        print("Cliente actualizado")

    def eliminar_cliente(self, email):
        cliente = self.buscar_cliente(email)

        if cliente is None:
            print("Cliente no encontrado")
            return

        self.clientes.remove(cliente)
        self.guardar_log("Cliente eliminado: " + email)
        print("Cliente eliminado")

    def guardar_csv(self):
        try:
            with open("clientes.csv", "w", encoding="utf-8") as archivo:
                archivo.write("nombre,email,telefono,direccion,tipo\n")

                for cliente in self.clientes:
                    linea = cliente.nombre + "," + cliente.obtener_email() + "," + cliente.telefono + "," + cliente.direccion + "," + cliente.tipo_cliente() + "\n"
                    archivo.write(linea)

            self.guardar_log("Clientes guardados en CSV")
            print("Datos guardados en clientes.csv")
        except Exception as error:
            print("Error al guardar el archivo:", error)

    def cargar_csv(self):
        try:
            with open("clientes.csv", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

            self.clientes = []

            for linea in lineas[1:]:
                datos = linea.strip().split(",")

                if len(datos) == 5:
                    nombre = datos[0]
                    email = datos[1]
                    telefono = datos[2]
                    direccion = datos[3]
                    tipo = datos[4]

                    if tipo == "Regular":
                        cliente = ClienteRegular(nombre, email, telefono, direccion)
                    elif tipo == "Premium":
                        cliente = ClientePremium(nombre, email, telefono, direccion)
                    else:
                        cliente = ClienteCorporativo(nombre, email, telefono, direccion)

                    self.clientes.append(cliente)

            print("Datos cargados desde clientes.csv")
        except FileNotFoundError:
            print("El archivo clientes.csv no existe")
        except Exception as error:
            print("Error al leer el archivo:", error)

    def guardar_log(self, mensaje):
        with open("registro.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje + "\n")
