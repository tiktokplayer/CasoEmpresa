import clases.empleado as empleado
import clases.departamento as departamento

class Asignacion():
    def __init__(self, id_asignacion, id_departamento, id_empleado):
        self.id_asignacion = id_asignacion
        super().__init__(id_departamento)
        super().__init__(id_empleado)
    
    #def Validar_asignacion():
    #def Asignacion():