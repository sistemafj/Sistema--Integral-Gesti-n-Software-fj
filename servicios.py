from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):
        if tarifa_base <= 0:
            raise ValueError("La tarifa debe ser mayor que cero.")

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass

    @abstractmethod
    def mostrar_descripcion(self):
        pass


class ReservaHabitacion(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        subtotal = self.tarifa_base * duracion
        return subtotal - (subtotal * descuento / 100)

    def mostrar_descripcion(self):
        return f"Reserva de habitación: {self.nombre}"


class AlquilerEquipos(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        subtotal = self.tarifa_base * duracion
        return subtotal - (subtotal * descuento / 100)

    def mostrar_descripcion(self):
        return f"Alquiler de equipos: {self.nombre}"


class ConsultoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        subtotal = self.tarifa_base * duracion
        return subtotal - (subtotal * descuento / 100)

    def mostrar_descripcion(self):
        return f"Consultoría especializada: {self.nombre}"