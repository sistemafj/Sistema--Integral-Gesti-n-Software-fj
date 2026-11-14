from abc import ABC, abstractmethod
from numbers import Real


class Servicio(ABC):
    """
    Clase abstracta que representa los servicios de Software FJ.
    """

    def __init__(self, nombre, tarifa_base):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        if (
            not isinstance(tarifa_base, Real)
            or isinstance(tarifa_base, bool)
            or tarifa_base <= 0
        ):
            raise ValueError("La tarifa debe ser un número mayor que cero.")

        self.nombre = nombre.strip()
        self.tarifa_base = tarifa_base

    def validar_parametros(self, duracion, descuento, impuesto):
        """Valida los datos utilizados para calcular el costo."""

        if (
            not isinstance(duracion, Real)
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        if (
            not isinstance(descuento, Real)
            or isinstance(descuento, bool)
            or not 0 <= descuento <= 100
        ):
            raise ValueError("El descuento debe estar entre 0 y 100.")

        if (
            not isinstance(impuesto, Real)
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 100
        ):
            raise ValueError("El impuesto debe estar entre 0 y 100.")

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def mostrar_descripcion(self):
        """Describe el servicio ofrecido."""
        pass


class ReservaHabitacion(Servicio):
    """Servicio especializado en reservas de habitaciones."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion, descuento, impuesto)

        subtotal = self.tarifa_base * duracion
        valor_descuento = subtotal * descuento / 100
        base_imponible = subtotal - valor_descuento
        total = base_imponible + (base_imponible * impuesto / 100)

        return total

    def mostrar_descripcion(self):
        return f"Reserva de habitación: {self.nombre}"


class AlquilerEquipos(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion, descuento, impuesto)

        subtotal = self.tarifa_base * duracion
        cargo_adicional = subtotal * 0.05
        subtotal += cargo_adicional

        valor_descuento = subtotal * descuento / 100
        base_imponible = subtotal - valor_descuento
        total = base_imponible + (base_imponible * impuesto / 100)

        return total

    def mostrar_descripcion(self):
        return f"Alquiler de equipos: {self.nombre}"


class ConsultoriaEspecializada(Servicio):
    """Servicio especializado en consultorías."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion, descuento, impuesto)

        subtotal = self.tarifa_base * duracion
        valor_descuento = subtotal * descuento / 100
        base_imponible = subtotal - valor_descuento
        total = base_imponible + (base_imponible * impuesto / 100)

        return total

    def mostrar_descripcion(self):
        return f"Consultoría especializada: {self.nombre}"