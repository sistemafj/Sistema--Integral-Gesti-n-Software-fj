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
    ServicioNoValido
)
from registro import RegistroOperaciones


gestor_errores = GestorErrores()
historial = RegistroOperaciones()

cliente = None
servicio = None
reserva = None
reserva_pendiente = None


def registrar_operacion(numero, descripcion, resultado="Correcta"):
    print(f"\nOPERACIÓN {numero}: {descripcion}")
    print(f"Resultado: {resultado}")
    historial.registrar(descripcion, resultado)


def registrar_fallo(error, descripcion):
    gestor_errores.registrar_error(error, descripcion)
    registrar_operacion(
        numero_actual,
        descripcion,
        "Fallida"
    )


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
    registrar_operacion(1, "Registro de cliente válido")

except Exception as error:
    gestor_errores.registrar_error(error, "Registro de cliente")
    registrar_operacion(1, "Registro de cliente válido", "Fallida")


# OPERACIÓN 2: Intentar registrar un cliente inválido
numero_actual = 2
try:
    Cliente("C002", "Ana López", "correo_incorrecto", "3001234567")

except ValueError as error:
    try:
        raise ClienteNoValido(
            "No se pudo registrar el cliente por datos incorrectos."
        ) from error
    except ClienteNoValido as error_personalizado:
        registrar_fallo(error_personalizado, "Registro de cliente inválido")


# OPERACIÓN 3: Crear servicio de habitaciones
try:
    servicio = ReservaHabitacion("Habitación individual", 100000)
    registrar_operacion(3, "Creación de servicio de habitaciones")

except Exception as error:
    gestor_errores.registrar_error(error, "Crear servicio")
    registrar_operacion(3, "Crear servicio de habitaciones", "Fallida")


# OPERACIÓN 4: Crear servicio de alquiler de equipos
try:
    equipo = AlquilerEquipos("Computador portátil", 50000)
    registrar_operacion(4, "Creación de servicio de alquiler de equipos")

except Exception as error:
    gestor_errores.registrar_error(error, "Crear servicio")
    registrar_operacion(4, "Crear servicio de equipos", "Fallida")


# OPERACIÓN 5: Crear servicio de consultoría
try:
    consultoria = ConsultoriaEspecializada("Asesoría técnica", 150000)
    registrar_operacion(5, "Creación de servicio de consultoría")

except Exception as error:
    gestor_errores.registrar_error(error, "Crear servicio")
    registrar_operacion(5, "Crear servicio de consultoría", "Fallida")


# OPERACIÓN 6: Intentar crear un servicio inválido
numero_actual = 6
try:
    ReservaHabitacion("Habitación inválida", 0)

except ValueError as error:
    try:
        raise ServicioNoValido(
            "La tarifa del servicio debe ser mayor que cero."
        ) from error
    except ServicioNoValido as error_personalizado:
        registrar_fallo(error_personalizado, "Creación de servicio inválido")


# OPERACIÓN 7: Crear una reserva
try:
    reserva = Reserva("R001", cliente, servicio, 2)
    registrar_operacion(7, "Creación de reserva R001")

except Exception as error:
    gestor_errores.registrar_error(error, "Crear reserva")
    registrar_operacion(7, "Creación de reserva", "Fallida")


# OPERACIÓN 8: Confirmar la reserva
try:
    print(reserva.confirmar())
    registrar_operacion(8, "Confirmación de reserva R001")

except Exception as error:
    gestor_errores.registrar_error(error, "Confirmar reserva")
    registrar_operacion(8, "Confirmación de reserva", "Fallida")


# OPERACIÓN 9: Procesar la reserva
try:
    costo = reserva.procesar(descuento=10)
    print(f"Costo final de la reserva: ${costo:,.0f}")
    registrar_operacion(9, "Procesamiento de reserva R001")

except Exception as error:
    gestor_errores.registrar_error(error, "Procesar reserva")
    registrar_operacion(9, "Procesamiento de reserva", "Fallida")


# OPERACIÓN 10: Crear una segunda reserva pendiente
try:
    reserva_pendiente = Reserva("R002", cliente, equipo, 1)
    registrar_operacion(10, "Creación de reserva R002")

except Exception as error:
    gestor_errores.registrar_error(error, "Crear segunda reserva")
    registrar_operacion(10, "Creación de reserva R002", "Fallida")


# OPERACIÓN 11: Intentar procesar una reserva sin confirmar
numero_actual = 11
try:
    reserva_pendiente.procesar()

except ValueError as error:
    registrar_fallo(error, "Procesamiento de reserva sin confirmar")


# OPERACIÓN 12: Cancelar la segunda reserva
try:
    print(reserva_pendiente.cancelar())
    registrar_operacion(12, "Cancelación de reserva R002")

except Exception as error:
    gestor_errores.registrar_error(error, "Cancelar reserva")
    registrar_operacion(12, "Cancelación de reserva R002", "Fallida")


# RESUMEN FINAL
print("\n" + "=" * 60)
print("              RESUMEN DEL SISTEMA")
print("=" * 60)

print("\nInformación del cliente:")
if cliente is not None:
    print(cliente.mostrar_informacion())

print("\nResumen de la primera reserva:")
if reserva is not None:
    print(reserva.mostrar_resumen())

print("\nHistorial de operaciones:")
historial.mostrar_historial()

print("\nHistorial de errores:")
gestor_errores.mostrar_errores()

# Guardar registros
try:
    historial.guardar_historial()
    gestor_errores.guardar_errores()

except Exception as error:
    print(f"Error al guardar los registros: {error}")

finally:
    print("\n" + "=" * 60)
    print("       SISTEMA SOFTWARE FJ - PROCESO FINALIZADO")
    print("=" * 60)