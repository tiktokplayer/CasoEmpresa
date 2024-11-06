from clases.empleado import Empleado as empleado

class Departamento:
    def __init__(self, id_departamento, nom_departamento, id_empleado):
        self.id_departamento = id_departamento
        self.nom_departamento = nom_departamento
        self.empleado = empleado(id_empleado)