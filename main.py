def calcular_costo_ruta(mapa, ruta, tipo_vehiculo, peajes, tarifa_peaje=5.0):
    costo_total=0.0

    for fila, columna in ruta:
        valor = mapa[fila][columna]
        costo_celda=0.0

        #calculo de celda segun semaforo o tafico

        if valor < 0:
            segundos=-valor
            if tipo_vehiculo.lower()=="camion":
                costo_celda=segundos * 0.5
            else:
                costo_celda=0.0
        else:
            if tipo_vehiculo.lower()=="camion":
                costo_celda= valor*2,5
            else:
                costo_celda=1.2**valor

        #peaje

        if (fila, columna) in peajes:
            costo_celda += tarifa_peaje

        costo_total += costo_celda

    return costo_total
    

