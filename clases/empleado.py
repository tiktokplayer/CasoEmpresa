from clases.tipo_empleado import Tipoempleado as tipo_empleado
from clases.roles import Roles as roles


class Empleado(tipo_empleado, roles):
    def __init__(self, id_empleado, nom_empleado, correo, telefono, direccion, rut, 
                 fecha_nacimiento, fecha_contrato, salario, id_tipo_empleado, 
                 id_roles, password_emp):
        super().__init__(id_tipo_empleado)
        super().__init__(id_roles)
        self.id_empleado = id_empleado
        self.nom_empleado = nom_empleado
        self.rut = rut
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_contrato = fecha_contrato
        self.salario = salario
        self.password_emp = password_emp

    
    #def Validar_datos():
    #def Habilitar_modulos():
    #def encriptacion():