from entidad import Entidad


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        if not nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")

        if "@" not in correo:
            raise ValueError("El correo electrónico no es válido.")

        if not telefono.isdigit():
            raise ValueError("El teléfono debe contener solamente números.")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

    def actualizar_correo(self, nuevo_correo):
        if "@" not in nuevo_correo:
            raise ValueError("El correo electrónico no es válido.")

        self.__correo = nuevo_correo