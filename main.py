from cliente import Cliente
from servicios import (
    ReservaHabitacion,
    AlquilerEquipos,
    ConsultoriaEspecializada
)
from reserva import Reserva
from excepciones import (
    GestorErrores,
    ClienteNoValido,
    ServicioNoValido,
    ReservaNoValida
)
from registro import RegistroOperaciones


# Inicialización de los gestores del sistema
gestor_errores = GestorErrores()
historial = RegistroOperaciones()

cliente = None
servicio = None
equipo = None
consultoria = None
reserva = None
reserva_pendiente = None


def registrar_operacion(numero, descripcion, resultado="Correcta"):
    """Registra y muestra el resultado de una operación."""

    print(f"\nOPERACIÓN {numero}: {descripcion}")
    print(f"Resultado: {resultado}")
    historial.registrar(descripcion, resultado)


def registrar_fallo(numero, error, descripcion):
    """Registra un error sin detener la ejecución del sistema."""

    print(f"\nOPERACIÓN {numero}: {descripcion}")
    gestor_errores.registrar_error(error, descripcion)
    historial.registrar(descripcion, "Fallida")


print("=" * 60)
print("       SOFTWARE FJ - SISTEMA INTEGRAL DE GESTIÓN")
print("=" * 60)


# OPERACIÓN 1: Registrar un cliente válido
try:
    cliente = Cliente(
        "C001",
        "Carlos Pérez",
        "carlos@gmail.com",
        "3001234567"
    )
    historial.agregar_cliente(cliente)

except Exception as error:
    registrar_fallo(1, error, "Registro de cliente válido")

else:
    registrar_operacion(1, "Registro de cliente válido")


# OPERACIÓN 2: Intentar registrar un cliente inválido
try:
    Cliente("C002", "Ana López", "correo_incorrecto", "3001234567")

except ValueError as error:
    try:
        raise ClienteNoValido(
            "No se pudo registrar el cliente por datos incorrectos."
        ) from error

    except ClienteNoValido as error_personalizado:
        registrar_fallo(
            2, error_personalizado, "Registro de cliente inválido"
        )

except Exception as error:
    registrar_fallo(2, error, "Registro de cliente inválido")

else:
    registrar_operacion(2, "Registro de cliente inválido")


# OPERACIÓN 3: Crear servicio de habitaciones
try:
    servicio = ReservaHabitacion("Habitación individual", 100000)
    historial.agregar_servicio(servicio)

except Exception as error:
    registrar_fallo(3, error, "Creación de servicio de habitaciones")

else:
    registrar_operacion(3, "Creación de servicio de habitaciones")


# OPERACIÓN 4: Crear servicio de alquiler de equipos
try:
    equipo = AlquilerEquipos("Computador portátil", 50000)
    historial.agregar_servicio(equipo)

except Exception as error:
    registrar_fallo(4, error, "Creación de servicio de alquiler de equipos")

else:
    registrar_operacion(4, "Creación de servicio de alquiler de equipos")


# OPERACIÓN 5: Crear servicio de consultoría
try:
    consultoria = ConsultoriaEspecializada("Asesoría técnica", 150000)
    historial.agregar_servicio(consultoria)

except Exception as error:
    registrar_fallo(5, error, "Creación de servicio de consultoría")

else:
    registrar_operacion(5, "Creación de servicio de consultoría")


# OPERACIÓN 6: Intentar crear un servicio inválido
try:
    ReservaHabitacion("Habitación inválida", 0)

except ValueError as error:
    try:
        raise ServicioNoValido(
            "La tarifa del servicio debe ser mayor que cero."
        ) from error

    except ServicioNoValido as error_personalizado:
        registrar_fallo(
            6, error_personalizado, "Creación de servicio inválido"
        )

except Exception as error:
    registrar_fallo(6, error, "Creación de servicio inválido")

else:
    registrar_operacion(6, "Creación de servicio inválido")


# OPERACIÓN 7: Crear una reserva
try:
    if cliente is None or servicio is None:
        raise ValueError("No hay cliente o servicio disponible.")

    reserva = Reserva("R001", cliente, servicio, 2)
    historial.agregar_reserva(reserva)

except Exception as error:
    registrar_fallo(7, error, "Creación de reserva R001")

else:
    registrar_operacion(7, "Creación de reserva R001")


# OPERACIÓN 8: Confirmar la reserva
try:
    if reserva is None:
        raise ValueError("No existe una reserva para confirmar.")

    print(reserva.confirmar())

except Exception as error:
    registrar_fallo(8, error, "Confirmación de reserva R001")

else:
    registrar_operacion(8, "Confirmación de reserva R001")


# OPERACIÓN 9: Procesar la reserva con descuento e impuesto
try:
    if reserva is None:
        raise ValueError("No existe una reserva para procesar.")

    costo = reserva.procesar(descuento=10, impuesto=0)
    print(f"Costo final de la reserva: ${costo:,.0f}")

except Exception as error:
    registrar_fallo(9, error, "Procesamiento de reserva R001")

else:
    registrar_operacion(9, "Procesamiento de reserva R001")


# OPERACIÓN 10: Crear una segunda reserva pendiente
try:
    if cliente is None or equipo is None:
        raise ValueError("No hay cliente o equipo disponible.")

    reserva_pendiente = Reserva("R002", cliente, equipo, 1)
    historial.agregar_reserva(reserva_pendiente)

except Exception as error:
    registrar_fallo(10, error, "Creación de reserva R002")

else:
    registrar_operacion(10, "Creación de reserva R002")


# OPERACIÓN 11: Intentar procesar una reserva sin confirmar
try:
    if reserva_pendiente is None:
        raise ValueError("No existe la segunda reserva.")

    reserva_pendiente.procesar()

except Exception as error:
    try:
        raise ReservaNoValida(
            "No se puede procesar una reserva sin confirmar."
        ) from error

    except ReservaNoValida as error_personalizado:
        registrar_fallo(
            11,
            error_personalizado,
            "Procesamiento de reserva sin confirmar"
        )

else:
    registrar_operacion(11, "Procesamiento de reserva sin confirmar")


# OPERACIÓN 12: Cancelar la segunda reserva
try:
    if reserva_pendiente is None:
        raise ValueError("No existe una reserva para cancelar.")

    print(reserva_pendiente.cancelar())

except Exception as error:
    registrar_fallo(12, error, "Cancelación de reserva R002")

else:
    registrar_operacion(12, "Cancelación de reserva R002")


# RESUMEN FINAL DEL SISTEMA
print("\n" + "=" * 60)
print("              RESUMEN DEL SISTEMA")
print("=" * 60)

print("\nInformación del cliente:")
if cliente is not None:
    print(cliente.mostrar_informacion())
else:
    print("No se pudo registrar el cliente.")

print("\nResumen de la primera reserva:")
if reserva is not None:
    print(reserva.mostrar_resumen())
else:
    print("No se pudo crear la primera reserva.")

print("\nCantidad de clientes:", len(historial.clientes))
print("Cantidad de servicios:", len(historial.servicios))
print("Cantidad de reservas:", len(historial.reservas))

print("\nHistorial de operaciones:")
historial.mostrar_historial()

print("\nHistorial de errores:")
gestor_errores.mostrar_errores()


# GUARDAR LOS REGISTROS DEL SISTEMA
try:
    historial.guardar_historial()
    gestor_errores.guardar_errores()

except Exception as error:
    print(f"Error al guardar los registros: {error}")

else:
    print("Todos los procesos de guardado fueron ejecutados.")

finally:
    print("\n" + "=" * 60)
    print("       SISTEMA SOFTWARE FJ - PROCESO FINALIZADO")
    print("=" * 60)