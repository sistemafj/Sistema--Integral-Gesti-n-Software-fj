from datetime import datetime


class RegistroOperaciones:
    """
    Administra las operaciones y las colecciones internas
    de clientes, servicios y reservas.
    """

    def __init__(self):
        self.operaciones = []
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar(self, descripcion, resultado="Correcta"):
        """Guarda una operación con su fecha y resultado."""

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        operacion = {
            "fecha": fecha,
            "descripcion": descripcion,
            "resultado": resultado
        }

        self.operaciones.append(operacion)

    def agregar_cliente(self, cliente):
        """Agrega un cliente a la colección interna."""

        if cliente in self.clientes:
            raise ValueError("El cliente ya está registrado.")

        self.clientes.append(cliente)

    def agregar_servicio(self, servicio):
        """Agrega un servicio a la colección interna."""

        if servicio in self.servicios:
            raise ValueError("El servicio ya está registrado.")

        self.servicios.append(servicio)

    def agregar_reserva(self, reserva):
        """Agrega una reserva a la colección interna."""

        if reserva in self.reservas:
            raise ValueError("La reserva ya está registrada.")

        self.reservas.append(reserva)

    def mostrar_historial(self):
        """Muestra todas las operaciones realizadas."""

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
        """Guarda el historial de operaciones en un archivo."""

        try:
            with open(archivo, "w", encoding="utf-8") as documento:
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