
19 lines (17 sloc) 732 Bytes
operaciones = [linea.rstrip('\n') for linea in open('../Datos/operacion.csv')]
retrasos =  [linea.rstrip('\n') for linea in open('../Datos/retraso.csv')]
operaciones_validas = []
for linea in operaciones:
    trozos = linea.split(',')
operaciones_validas.append((trozos[0],trozos[6], trozos[5]))