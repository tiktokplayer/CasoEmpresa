from datetime import datetime

class Proyecto():
    def __init__(self, id_proyecto, nom_proyecto, des_proyecto, fecha_inicio, fecha_fin):
        self.id_proyecto = id_proyecto
        self.nom_proyecto = nom_proyecto
        self.des_proyecto = des_proyecto
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    #def Validar_fechas():
