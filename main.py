from mysql.connector import connect
import submenu as sm
from clases.empleado import Empleado
from clases.departamento import Departamento
from clases.informe import Informe
from clases.roles import Roles
from clases.tipo_empleado import Tipoempleado
from servicios.consultar_apis import consultar_api as api
import requests as req

# clases, modulo empleado, conección a base de datos, informacion de base de datos

def menu(cnx):
    while True:
        print("\nMenu principal")
        print("1. Menu Empleados")
        print("2. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            sm.menu_empleado(cnx)
        elif opcion == "2":
            break
        else:
            print("Opcion no valida")

def main():
    try:
        # Conectar a la base de datos
        cnx = connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="caso_empresa"
        )
        
        if cnx.is_connected():
            print("Conexión exitosa a la base de datos")
            print("Bienvenido al Sistema")
            menu(cnx)
        else:
            print("No se pudo conectar a la base de datos")
            return

    except Exception as e:
        print(f"Error de conexión: {e}")
    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()
            print("\nConexión cerrada")

if __name__ == "__main__":
    main()

# def api():
#     try:
#         rut = input("Ingrese el RUT: ")
#         response = req.get(f"https://api.boostr.cl/rut/name/{rut}.json")
#         print(response.text)
#     except Exception as e:
#         print(f"Error al consultar la API: {e}")


# if __name__ == "__main__":
#     api()