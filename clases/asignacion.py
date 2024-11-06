from clases.departamento import Departamento as departamento
from clases.empleado import Empleado as empleado


class Asignacion:
    def __init__(self, id_asignacion, id_departamento, id_empleado):
        self.id_asignacion = id_asignacion
        self.departamento = departamento(id_departamento)
        self.empleado = empleado(id_empleado)
    
    #def Validar_asignacion():
    #def Asignacion():