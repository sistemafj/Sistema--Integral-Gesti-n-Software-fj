from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    del sistema Software FJ.
    """

    def __init__(self, identificador):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador no puede estar vacío.")

        self.identificador = identificador.strip()

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método que deben implementar las clases derivadas.
        """
        pass