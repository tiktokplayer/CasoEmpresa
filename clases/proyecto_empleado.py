from clases.empleado import Empleado as empleado
from clases.proyecto import Proyecto as proyecto


class Proyecto_empleado(empleado, proyecto):
    def __init__(self, id_pro_empleado, id_empleado, id_proyecto):
        self.id_pro_empleado = id_pro_empleado
        super().__init__(id_empleado)
        super().__init__(id_proyecto)
