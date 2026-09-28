def calcular_costo_ruta(mapa, ruta, tipo_vehiculo, peajes, tarifa_peaje=5.0):
    if not ruta:
        return 0.0

    #validacion
    if tipo_vehiculo.lower() not in ("camion", "auto"):
        print("Error: Tipo de vehiculo invalido.")
        return None
    
    costo_total = 0.0
    filas = len(mapa)
    columnas = len(mapa[0]) if filas > 0 else 0

    for fila, columna in ruta:
        # Metodo de seguridad caso limite: control de indices
        if not (0 <= fila < filas and 0 <= columna < columnas):
            print(f"Error: Coordenada ({fila}, {columna}) fuera de los limites del mapa.")
            return None
        
        valor = mapa[fila][columna]
        costo_celda = 0.0

        # Calculo de celda segun semaforo o trafico
        if valor < 0:
            segundos = -valor
            if tipo_vehiculo.lower() == "camion":
                costo_celda = segundos * 1.5
            else:
                costo_celda = 0.0
        else:
            if tipo_vehiculo.lower() == "camion":
                costo_celda = valor * 2.5
            else:
                costo_celda = 1.2 ** valor

        # Peaje
        if (fila, columna) in peajes:
            costo_celda += tarifa_peaje

        costo_total += costo_celda

    return round(costo_total, 2)

    


mapa_ciudad = [
    [2, -15, 4],
    [4,   3, -10],
    [1,   8, 0]
]
    
peajes_ciudad = [(1, 1)]

print("EJECUCION DE PRUEBAS")

ruta_1 = [(0, 0), (0, 1), (1, 1)]

print("\nPRUEBA 1: Caso Estándar - Ruta mixta con peaje y semáforo")
costo_camion = calcular_costo_ruta(mapa_ciudad, ruta_1, "camion", peajes_ciudad, tarifa_peaje=5.0)
costo_auto = calcular_costo_ruta(mapa_ciudad, ruta_1, "auto", peajes_ciudad, tarifa_peaje=5.0)
print(f"Ruta: {ruta_1}")
print(f"- Costo Camión de carga: {costo_camion} unidades")
print(f"- Costo Auto eléctrico:  {costo_auto} unidades")

print("\nPRUEBA 2: Caso Límite - Ruta vacía")
ruta_vacia = []
costo_vacio = calcular_costo_ruta(mapa_ciudad, ruta_vacia, "auto", peajes_ciudad)
print(f"Ruta: {ruta_vacia}")
print(f"- Costo obtenido: {costo_vacio} unidades (Comportamiento correcto sin fallos)")

print("\nPRUEBA 3: Caso Límite - Coordenada fuera de límites")
ruta_invalida = [(0, 0), (5, 5)]  # (5, 5) no existe en una matriz 3x3
costo_invalido = calcular_costo_ruta(mapa_ciudad, ruta_invalida, "camion", peajes_ciudad)
print(f"Ruta: {ruta_invalida}")
print(f"- Resultado: {costo_invalido} (Manejado con mensaje de advertencia)")
