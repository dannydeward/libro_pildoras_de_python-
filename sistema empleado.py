class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def mostrar_info(self):
        print(f"{self.nombre} gana ${self.sueldo}")

    def aumentar_sueldo(self, porcentaje):
        self.sueldo += self.sueldo * porcentaje / 100

e = Empleado("Carlos", 50000)
e.aumentar_sueldo(5)
e.mostrar_info()
