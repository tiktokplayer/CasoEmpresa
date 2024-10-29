import empleado
import proyecto


class Proyecto_empleado():
    def __init__(self, id_pro_empleado, id_empleado, id_proyecto):
        self.id_pro_empleado = id_pro_empleado
        super().__init__(id_empleado)
        super().__init__(id_proyecto)
