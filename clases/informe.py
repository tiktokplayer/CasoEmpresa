from clases.empleado import Empleado as empleado

class Informe(empleado):
    def __init__(self, id_empleado, id_informe, fecha_hora, reporte):
        super().__init__(id_empleado)
        self.id_informe = id_informe
        self.fecha_hora = fecha_hora
        self.reporte = reporte
    
    #  def generar_informe
    #  def exportar_informe

