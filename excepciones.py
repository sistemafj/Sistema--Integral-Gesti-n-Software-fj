from datetime import datetime


class ErrorSistema(Exception):
    """Excepción general del sistema Software FJ."""
    pass


class ClienteNoValido(ErrorSistema):
    """Error cuando los datos del cliente no son válidos."""
    pass


class ServicioNoValido(ErrorSistema):
    """Error cuando los datos del servicio no son válidos."""
    pass


class ReservaNoValida(ErrorSistema):
    """Error cuando una reserva no cumple las condiciones."""
    pass


class GestorErrores:
    """Administra y almacena los errores del sistema."""

    def __init__(self):
        self.errores = []

    def registrar_error(self, error, operacion=""):
        """Registra un error con fecha, operación y descripción."""

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        mensaje = (
            f"[{fecha}] "
            f"Operación: {operacion} | "
            f"Error: {type(error).__name__} | "
            f"Detalle: {error}"
        )

        self.errores.append(mensaje)
        print("Error registrado correctamente.")

    def procesar_error(self, error, operacion=""):
        """Registra una excepción personalizada encadenada."""

        try:
            raise ReservaNoValida(
                f"Error durante la operación: {operacion}"
            ) from error

        except ReservaNoValida as error_encadenado:
            self.registrar_error(error_encadenado, operacion)

    def mostrar_errores(self):
        """Muestra todos los errores registrados."""

        if not self.errores:
            print("No se han registrado errores.")
            return

        print("\n--- HISTORIAL DE ERRORES ---")

        for error in self.errores:
            print(error)

    def guardar_errores(self, archivo="registro_errores.txt"):
        """Guarda los errores de la ejecución actual."""

        try:
            with open(archivo, "w", encoding="utf-8") as documento:
                for error in self.errores:
                    documento.write(error + "\n")

        except OSError as error:
            print(f"No se pudo guardar el registro: {error}")

        else:
            print("Historial de errores guardado correctamente.")

        finally:
            print("Proceso de registro finalizado.")