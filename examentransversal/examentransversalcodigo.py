import random
import statistics

# Lista de nombres de los trabajadores
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función para asignar sueldos aleatorios
def asignar_sueldos_aleatorios():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos

# Función para clasificar sueldos
def clasificar_sueldos(sueldos):
    sueldos_menores = []
    sueldos_intermedios = []
    sueldos_superiores = []

    for sueldo in sueldos:
        if sueldo < 800000:
            sueldos_menores.append(sueldo)
        elif 800000 <= sueldo <= 2000000:
            sueldos_intermedios.append(sueldo)
        else:
            sueldos_superiores.append(sueldo)

    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(sueldos_menores)}")
    for i, sueldo in enumerate(sueldos_menores, start=1):
        print(f"{trabajadores[i-1]} ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(sueldos_intermedios)}")
    for i, sueldo in enumerate(sueldos_intermedios, start=1):
        print(f"{trabajadores[i-1]} ${sueldo}")

    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(sueldos_superiores)}")
    for i, sueldo in enumerate(sueldos_superiores, start=1):
        print(f"{trabajadores[i-1]} ${sueldo}")

    total_sueldos = sum(sueldos)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

# Función para mostrar estadísticas
def mostrar_estadisticas(sueldos):
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = statistics.mean(sueldos)
    media_geometrica = statistics.geometric_mean(sueldos)

    print("\nEstadísticas de sueldos:")
    print(f"Sueldo más alto: ${sueldo_maximo}")
    print(f"Sueldo más bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geométrica: ${media_geometrica:.2f}")

# Función para generar el reporte de sueldos
def generar_reporte(sueldos):
    with open("reporte_sueldos.csv", "w") as archivo_csv:
        archivo_csv.write("Nombre empleado,Sueldo líquido\n")
        for i, sueldo in enumerate(sueldos, start=1):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            archivo_csv.write(f"{trabajadores[i-1]},{sueldo_liquido:.2f}\n")
    print("\nReporte de sueldos generado en 'reporte_sueldos.csv'")

# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            sueldos_empleados = asignar_sueldos_aleatorios()
            print("\nSueldos aleatorios asignados.")
        elif opcion == "2":
            clasificar_sueldos(sueldos_empleados)
        elif opcion == "3":
            mostrar_estadisticas(sueldos_empleados)
        elif opcion == "4":
            generar_reporte(sueldos_empleados)
        elif opcion == "5":
            print("\nFinalizando Programa...\nDesarrollado por Claudio Aro\nRut 22022498-8")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
menu()
