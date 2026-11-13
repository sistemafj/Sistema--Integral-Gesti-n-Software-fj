from datetime import datetime


class ErrorSistema(Exception):
    """Excepción general del sistema Software FJ."""
    pass


class ClienteNoValido(ErrorSistema):
    pass


class ServicioNoValido(ErrorSistema):
    pass


class ReservaNoValida(ErrorSistema):
    pass


class GestorErrores:

    def __init__(self):
        self.errores = []

    def registrar_error(self, error, operacion=""):
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        mensaje = (
            f"[{fecha}] "
            f"Operación: {operacion} | "
            f"Error: {type(error).__name__} | "
            f"Detalle: {error}"
        )

        self.errores.append(mensaje)

        print("Error registrado correctamente.")

    def mostrar_errores(self):
        if not self.errores:
            print("No se han registrado errores.")
            return

        print("\n--- HISTORIAL DE ERRORES ---")

        for error in self.errores:
            print(error)

    def guardar_errores(self, archivo="registro_errores.txt"):
        try:
            with open(archivo, "a", encoding="utf-8") as documento:
                for error in self.errores:
                    documento.write(error + "\n")

        except OSError as error:
            print(f"No se pudo guardar el registro: {error}")

        else:
            print("Historial de errores guardado correctamente.")

        finally:
            print("Proceso de registro finalizado.")