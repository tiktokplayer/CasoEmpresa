class Registrotiempo():
    def __init__(self, id_registro, id_pro_empleado, fecha, cantidad_horas, des_reg_tiempo, horas_extras, observacion):
        self.id_registro = id_registro
        self.id_pro_empleado = id_pro_empleado
        self.fecha = fecha
        self.cantidad_horas = cantidad_horas
        self.des_reg_tiempo = des_reg_tiempo
        self.horas_extras = horas_extras
        self.observacion = observacion

    def validacion_cant_hrs(cant_hrs):
        max_horas_normales = 45
        if cant_hrs <= max_horas_normales:
            return {
            'horas_normales': cant_hrs,
            'horas_extras': 0
        }
        else:
            horas_extras = cant_hrs - max_horas_normales
            return {
            'horas_normales': max_horas_normales,
            'horas_extras': horas_extras
        }