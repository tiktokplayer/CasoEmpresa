from  mysql.connector import (connection)
from tabulate import tabulate

def agregar_empleado(cnx):
    id_empleado = int(input("Ingrese el ID del empleado: "))
    nombre = input("Ingrese el nombre del empleado: ")
    correo = input("Ingrese el correo del empleado: ")
    telefono = int(input("Ingrese el telefono del empleado: "))
    direccion = input("Ingrese la direccion del empleado: ")
    rut = input("Ingrese el RUT del empleado: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    fecha_contrato = input("Ingrese la fecha de contrato (YYYY-MM-DD): ")
    salario = int(input("Ingrese el salario del empleado: "))
    id_tipo_empleado = int(input("Ingrese el ID del tipo de empleado, 1 = Gerente, 2 = Desarrollador, 3 = Tester, 4 = Administrador, 5 = Empleado: "))
    id_roles = int(input("Ingrese el ID del rol, 1 = Gerente, 2 = Desarrollador, 3 = Tester, 4 = Administrador, 5 = Empleado: "))
    password_emp = input("Ingrese la contraseña del empleado: ")
    
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO empleado (ID_EMPLEADO, NOM_EMPLEADO, CORREO, TELEFONO, DIRECCION, RUT, FECHA_NACIMIENTO, FECHA_CONTRATO, SALARIO, ID_TIPO_EMPLEADO, ID_ROLES, PASSWORD_EMP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  (id_empleado, nombre, correo, telefono, direccion, rut, fecha_nacimiento, fecha_contrato, salario, id_tipo_empleado, id_roles, password_emp))
    cnx.commit()
    print("Empleado agregado exitosamente")
    cursor.close()


def ver_empleados(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM empleado")
    empleados = cursor.fetchall()
    headers = ["ID_EMPLEADO", "NOM_EMPLEADO", "CORREO", "TELEFONO", "DIRECCION", "RUT", "FECHA_NACIMIENTO", "FECHA_CONTRATO", "SALARIO", "ID_TIPO_EMPLEADO", "ID_ROLES", "PASSWORD_EMP"]
    if not empleados:
        print("No se encontraron empleados")
        return
    print(tabulate(empleados, headers=headers, tablefmt="pretty"))
    cursor.close()

def borrar_empleado(cnx):
    try:
        id_empleado = int(input("Ingrese el ID del empleado a borrar: "))
        cursor = cnx.cursor()
        
        # Verify if employee exists
        cursor.execute("SELECT ID_EMPLEADO FROM empleado WHERE ID_EMPLEADO = %s", (id_empleado,))
        if not cursor.fetchone():
            print("El empleado no existe")
            return
            
        cursor.execute("DELETE FROM empleado WHERE ID_EMPLEADO = %s", (id_empleado,))
        cnx.commit()
        print("Empleado borrado exitosamente")
    except ValueError:
        print("El ID debe ser un número")
    except Exception as e:
        print(f"Error al borrar empleado: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()

def actualizar_empleado(cnx):
    id_empleado = int(input("Ingrese el ID del empleado a actualizar: "))
    
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM empleado WHERE ID_EMPLEADO = %s", (id_empleado,))
    if not cursor.fetchone():
        print("No se encontró un empleado con ese ID")
        cursor.close()
        return
        
    nombre = input("Ingrese el nuevo nombre del empleado: ")
    correo = input("Ingrese el nuevo correo del empleado: ")
    telefono = int(input("Ingrese el nuevo telefono del empleado: "))
    direccion = input("Ingrese la nueva direccion del empleado: ")
    rut = int(input("Ingrese el nuevo RUT del empleado: "))
    fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ")
    fecha_contrato = input("Ingrese la nueva fecha de contrato (YYYY-MM-DD): ")
    salario = int(input("Ingrese el nuevo salario del empleado: "))
    id_tipo_empleado = int(input("Ingrese el nuevo ID del tipo de empleado: "))
    id_roles = int(input("Ingrese el nuevo ID del rol: "))
    password_emp = input("Ingrese la nueva contraseña del empleado: ")

    cursor.execute("UPDATE empleado SET NOM_EMPLEADO = %s, CORREO = %s, TELEFONO = %s, DIRECCION = %s, RUT = %s, FECHA_NACIMIENTO = %s, FECHA_CONTRATO = %s, SALARIO = %s, ID_TIPO_EMPLEADO = %s, ID_ROLES = %s, PASSWORD_EMP = %s WHERE ID_EMPLEADO = %s", 
                  (nombre, correo, telefono, direccion, rut, fecha_nacimiento, fecha_contrato, salario, id_tipo_empleado, id_roles, password_emp, id_empleado))
    
    cnx.commit()
    print("Empleado actualizado exitosamente")
    cursor.close()










# """
# cursor = cnx.cursor()
# cursor.execute("SELECT * FROM empleados")
# empleados = cnx.fetchall()
# hearders = ["ID","Nombre","Salary", etc..]
# cnx.commit()
# print(tabulate(empleados, headers=hearders, tablefmt="pretty", "rounded_outline"))
# """