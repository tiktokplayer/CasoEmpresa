from mysql.connector import connect
import submenu as sm


#clases, modulo empleado, conección a base de datos, informacion de base de datos

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
    cnx = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="")
    
    cur = cnx.cursor()

    cur.execute("SELECT CURDATE()")

    row = cur.fetchone()
    print("Current date is: {0}".format(row[0]))

    cnx.close()
