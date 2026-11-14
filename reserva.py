from datetime import datetime
from numbers import Real

from entidad import Entidad
from servicios import Servicio


class Reserva:
    """
    Representa una reserva de un cliente para un servicio.
    Controla su creación, confirmación, procesamiento y cancelación.
    """

    def __init__(self, codigo, cliente, servicio, duracion):

        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código de la reserva no puede estar vacío.")

        if not isinstance(cliente, Entidad):
            raise ValueError("La reserva necesita un cliente válido.")

        if not isinstance(servicio, Servicio):
            raise ValueError("La reserva necesita un servicio válido.")

        if (
            not isinstance(duracion, Real)
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        self.codigo = codigo.strip()
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.fecha = datetime.now()
        self.costo_final = None

    def confirmar(self):
        """Confirma una reserva que se encuentra pendiente."""

        if self.estado != "Pendiente":
            raise ValueError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.estado = "Confirmada"
        return f"Reserva {self.codigo} confirmada."

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.estado not in ("Pendiente", "Confirmada"):
            raise ValueError(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self.estado = "Cancelada"
        return f"Reserva {self.codigo} cancelada."

    def procesar(self, descuento=0, impuesto=0):
        """
        Procesa una reserva confirmada y calcula su costo.
        Permite utilizar descuentos e impuestos opcionales.
        """

        if self.estado != "Confirmada":
            raise ValueError(
                "La reserva debe estar confirmada para procesarse."
            )

        costo = self.servicio.calcular_costo(
            self.duracion,
            descuento,
            impuesto
        )

        self.costo_final = costo
        self.estado = "Procesada"

        return costo

    def mostrar_resumen(self):
        """Muestra la información completa de la reserva."""

        costo = (
            f"${self.costo_final:,.0f}"
            if self.costo_final is not None
            else "Pendiente de cálculo"
        )

        return (
            f"Reserva: {self.codigo}\n"
            f"Cliente: {self.cliente.mostrar_informacion()}\n"
            f"Servicio: {self.servicio.mostrar_descripcion()}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Costo: {costo}\n"
            f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"
        )