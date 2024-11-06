import funciones as fn
def menu_empleado(cnx):
    while True:
        print("\nMenu principal")
        print("1. Agregar empleado")
        print("2. Ver empleados")
        print("3. Borrar empleado")
        print("4. Actualizar empleado")
        print("5. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            fn.agregar_empleado(cnx)
        elif opcion == "2":
            fn.ver_empleados(cnx)
        elif opcion == "3":
            fn.borrar_empleado(cnx)
        elif opcion == "4":
            fn.actualizar_empleado(cnx)
        elif opcion == "5":
            break
        else:
            print("Opcion no valida")