import funciones as fn
def menu_empleado(cnx):
    while True:
        print("\nMenu principal")
        print("1. Agregar empleado")
        print("2. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            fn.agregar_empleado(cnx)
        elif opcion == "2":
            break
        else:
            print("Opcion no valida")