from clases.empleado import Empleado as empleado
from clases.proyecto import Proyecto as proyecto


class Proyectoempleado:
    def __init__(self, id_pro_empleado, id_empleado, id_proyecto):
        self.id_pro_empleado = id_pro_empleado
        self.empleado = empleado(id_empleado)
        self.proyecto = proyecto(id_proyecto)
