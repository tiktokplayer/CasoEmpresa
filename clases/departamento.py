from clases.empleado import Empleado as empleado

class Departamento(empleado):
    def __init__(self, id_departamento, nom_departamento, id_empleado):
        self.id_departamento = id_departamento
        self.nom_departamento = nom_departamento
        super().__init__(id_empleado)