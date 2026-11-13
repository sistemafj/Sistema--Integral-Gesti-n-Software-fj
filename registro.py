from datetime import datetime


class RegistroOperaciones:

    def __init__(self):
        self.operaciones = []

    def registrar(self, descripcion, resultado="Correcta"):
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        operacion = {
            "fecha": fecha,
            "descripcion": descripcion,
            "resultado": resultado
        }

        self.operaciones.append(operacion)

    def mostrar_historial(self):
        if not self.operaciones:
            print("No hay operaciones registradas.")
            return

        print("\n========== HISTORIAL DE OPERACIONES ==========")

        for numero, operacion in enumerate(self.operaciones, start=1):
            print(
                f"{numero}. [{operacion['fecha']}] "
                f"{operacion['descripcion']} - "
                f"{operacion['resultado']}"
            )

    def guardar_historial(self, archivo="historial_operaciones.txt"):
        try:
            with open(archivo, "a", encoding="utf-8") as documento:
                for operacion in self.operaciones:
                    documento.write(
                        f"[{operacion['fecha']}] "
                        f"{operacion['descripcion']} - "
                        f"{operacion['resultado']}\n"
                    )

        except OSError as error:
            print(f"No se pudo guardar el historial: {error}")

        else:
            print("Historial guardado correctamente.")

        finally:
            print("Proceso de historial finalizado.")