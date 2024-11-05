from clases.tipoempleado import Tipoempleado as tipoempleado
from clases.roles import Roles as roles


class Empleado(tipoempleado, roles):
    def __init__(self, id_empleado, nom_empleado, correo, telefono, direccion, rut, fecha_nacimiento, fecha_contrato, salario, id_tipo_empleado, id_roles, password):
        self.id_empleado = id_empleado
        self.nom_empleado = nom_empleado
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_contrato = fecha_contrato
        self.salario = salario
        super().__init__(id_tipo_empleado)
        super().__init__(id_roles)
        self.password = password

    
    #def Validar_datos():
    #def Habilitar_modulos():
    #def encriptacion():