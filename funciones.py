from tabulate import tabulate

"""
cursor = cnx.cursor()
cursor.execute("SELECT * FROM empleados")
empleados = cnx.fetchall()
hearders = ["ID","Nombre","Salary", etc..]
cnx.commit()
print(tabulate(empleados, headers=hearders, tablefmt="pretty", "rounded_outline"))

"""

def agregar_empleado(cnx):
    id_empleado = int(input("text: "))
    nombre = input("text: ")
    correo = input("text: ")
    telefono = input("text: ")
    cursor = cnx.cursor()
    cursor.execute("INSER...(ID_EMPLEADO,...) VALUES (%s, %s, %s, %s)",(id_empleado, nombre,correo,telefono))
    cnx.commit()
    print("Se agrego")