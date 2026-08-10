class Cliente:
    def __init__(self, nombre, email, telefono, direccion):
        self.nombre = nombre
        self.__email = email
        self.telefono = telefono
        self.direccion = direccion

    def obtener_email(self):
        return self.__email

    def cambiar_email(self, nuevo_email):
        if "@" in nuevo_email:
            self.__email = nuevo_email
            print("Correo actualizado")
        else:
            print("Correo no valido")

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Email:", self.__email)
        print("Telefono:", self.telefono)
        print("Direccion:", self.direccion)

    def tipo_cliente(self):
        return "Cliente"

    def __str__(self):
        return self.nombre + " - " + self.__email

    def __eq__(self, otro):
        return self.__email == otro.obtener_email()


class ClienteRegular(Cliente):
    def __init__(self, nombre, email, telefono, direccion):
        super().__init__(nombre, email, telefono, direccion)
        self.beneficio = "Cliente regular"

    def tipo_cliente(self):
        return "Regular"


class ClientePremium(Cliente):
    def __init__(self, nombre, email, telefono, direccion):
        super().__init__(nombre, email, telefono, direccion)
        self.beneficio = "Descuento 10%"

    def tipo_cliente(self):
        return "Premium"


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, telefono, direccion):
        super().__init__(nombre, email, telefono, direccion)
        self.beneficio = "Atencion corporativa"

    def tipo_cliente(self):
        return "Corporativo"
