import csv
import os

AREAS = ("TI", "Finanzas", "RRHH", "Comercial")


def listar_empleados(empleados):
    if not empleados:
        print("No hay empleados registrados")
        return

    for empleado in empleados:
        print(f"ID {empleado['id']} | Nombre {empleado['nombre']} | Edad {empleado['edad']} | Área {empleado['area']} | Tecnología {empleado['tecnologia']}")


def agregar_empleado(empleados, tecnologias):
    identificador = int(input("Ingrese un identificador: "))

    # Verificar si el ID ya existe
    for empleado in empleados:
        if empleado["id"] == identificador:
            print("Ese ID ya existe")
            return

    nombre = input("Ingrese el nombre: ")

    edad = int(input("Ingrese la edad: "))

    if edad <= 0:
        print("Edad incorrecta")
        return

    print("Elija el área:")

    for i, area in enumerate(AREAS, 1):
        print(f"{i}. {area}")

    opcion = int(input("Seleccione un área: "))

    if opcion < 1 or opcion > 4:
        print("Área no válida")
        return

    tecnologia = input("Ingrese la tecnología: ")

    empleado = {
        "id": identificador,
        "nombre": nombre,
        "edad": edad,
        "area": AREAS[opcion - 1],
        "tecnologia": tecnologia
    }

    empleados.append(empleado)
    tecnologias.add(tecnologia)

    guardar_csv(empleados)


def eliminar_empleado(empleados):
    identificador = int(input("Ingrese el ID del empleado a eliminar: "))

    for empleado in empleados:
        if empleado["id"] == identificador:
            empleados.remove(empleado)
            print("Empleado ha sido eliminado")

            guardar_csv(empleados)

            return

    print("No se encontró el empleado")


def mostrar_resumen(empleados, tecnologias):
    print(f"Total de empleados: {len(empleados)}")

    print("Listado de tecnologías:")

    for tecnologia in tecnologias:
        print(tecnologia)


def guardar_csv(empleados):
    with open("empleados.csv", "w", newline="", encoding="utf-8") as archivo:

        campos = ["id", "nombre", "edad", "area", "tecnologia"]

        escritor = csv.DictWriter(
            archivo,
            delimiter=";",
            fieldnames=campos
        )

        escritor.writeheader()
        escritor.writerows(empleados)

    print("Se generó el archivo empleados.csv")


def cargar_csv():
    empleados = []
    tecnologias = set()

    if not os.path.exists("empleados.csv"):
        return empleados, tecnologias

    with open("empleados.csv", "r", newline="", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo, delimiter=";")

        for empleado in lector:

            empleado["id"] = int(empleado["id"])
            empleado["edad"] = int(empleado["edad"])

            empleados.append(empleado)

            tecnologias.add(empleado["tecnologia"])

    print("Se han cargado los datos")

    return empleados, tecnologias
