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

def ver_empleados(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cnx.fetchall()
    headers = ["ID_EMPLEADO", "NOM_EMPLEADO", "CORREO", "TELEFONO", "DIRECCION", "RUT", "FECHA_NACIMIENTO", "FECHA_CONTRATO", "SALARIO", "ID_TIPO_EMPLEADO", "ID_ROLES", "PASSWORD_EMP"]
    print(tabulate(empleados, headers=headers, tablefmt="pretty", "rounded_outline"))

def borrar_empleado(cnx):
    id_empleado = int(input("Ingrese el ID del empleado a borrar: "))
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM empleados WHERE ID_EMPLEADO = %s", (id_empleado,))
    cnx.commit()
    print("Empleado borrado")

def actualizar_empleado(cnx):
    id_empleado = int(input("Ingrese el ID del empleado a actualizar: "))
    cursor = cnx.cursor()
    cursor.execute("UPDATE empleados SET NOM_EMPLEADO = %s, CORREO = %s, TELEFONO = %s, DIRECCION = %s, RUT = %s, FECHA_NACIMIENTO = %s, FECHA_CONTRATO = %s, SALARIO = %s, ID_TIPO_EMPLEADO = %s, ID_ROLES = %s, PASSWORD_EMP = %s WHERE ID_EMPLEADO = %s", (nombre, correo, telefono, direccion, rut, fecha_nacimiento, fecha_contrato, salario, id_tipo_empleado, id_roles, password_emp, id_empleado))
    cnx.commit()
    print("Empleado actualizado")
