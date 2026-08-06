from funciones import (
    listar_empleados,
    agregar_empleado,
    eliminar_empleado,
    buscar_empleado,
    mostrar_resumen,
    guardar_csv,
    cargar_csv
)
                        
def mostrar_menu():
    print("\nSistema de Gestión de Datos de Empleados")
    print("1. Agregar empleado")
    print("2. Listar empleados")
    print("3. Eliminar empleado")
    print("4. Buscar empleado")
    print("5. Mostrar resumen")
    print("6. Exportar datos")
    print("0. Salir")

def main():

    empleados, tecnologias = cargar_csv()

    while True:
        mostrar_menu()

        opcion = input("Ingrese una opción del menú [0..6]: ")

        if opcion == "1":
            print("Agregar empleado")
            agregar_empleado(empleados, tecnologias)
        elif opcion == "2":
            print("Listas empleados")
            
            listar_empleados(empleados)
        elif opcion == "3":
            print("Eliminar empleado")

            eliminar_empleado(empleados)
        elif opcion == "4":
            print("Buscar empleado")
            buscar_empleado(empleados)
          
        elif opcion == "5":
            print("Mostrar resumen")
            mostrar_resumen(empleados, tecnologias)

        elif opcion == "6":
            print("Exportar datos")
            guardar_csv(empleados)
            
        elif opcion == "0":
            break
        else:
            print("Opción no válida")

    print("Saliendo del sistema")

main()
