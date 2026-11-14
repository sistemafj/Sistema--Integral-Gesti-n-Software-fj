from entidad import Entidad


class Cliente(Entidad):
    """
    Representa un cliente del sistema Software FJ.
    Hereda de Entidad y protege sus datos personales.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")

        if not isinstance(correo, str) or "@" not in correo:
            raise ValueError("El correo electrónico no es válido.")

        if not isinstance(telefono, str) or not telefono.isdigit():
            raise ValueError("El teléfono debe contener solamente números.")

        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

    def mostrar_informacion(self):
        """Devuelve la información del cliente."""
        return (
            f"Identificador: {self.identificador} | "
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

    def actualizar_correo(self, nuevo_correo):
        """Actualiza el correo después de validar su formato."""
        if not isinstance(nuevo_correo, str) or "@" not in nuevo_correo:
            raise ValueError("El correo electrónico no es válido.")

        self.__correo = nuevo_correo.strip()