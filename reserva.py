from datetime import datetime


class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.fecha = datetime.now()

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ValueError("Solo se pueden confirmar reservas pendientes.")

        self.estado = "Confirmada"
        return f"Reserva {self.codigo} confirmada."

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ValueError("La reserva ya está cancelada.")

        self.estado = "Cancelada"
        return f"Reserva {self.codigo} cancelada."

    def procesar(self, descuento=0):
        if self.estado != "Confirmada":
            raise ValueError("La reserva debe estar confirmada para procesarse.")

        costo = self.servicio.calcular_costo(
            self.duracion, descuento
        )

        return costo

    def mostrar_resumen(self):
        return (
            f"Reserva: {self.codigo}\n"
            f"Cliente: {self.cliente.mostrar_informacion()}\n"
            f"Servicio: {self.servicio.mostrar_descripcion()}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"
        )