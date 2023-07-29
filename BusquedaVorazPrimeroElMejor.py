import time

grafo = {}

# obtenemos el grafo guardado
guardar = open('inst_Grafos.txt', 'r')
for i in range(20): # EL NUMERO SE CAMBIA SERGUN LA CANTIDAD DE NODOS
    xd = grafo.setdefault(str(i+1), eval(guardar.readline()))
    xd = grafo.setdefault(str("Distancias."+str(i+1)),eval(guardar.readline()))
guardar.close()

print("BUSQUEDA VORAZ PRIMERO EL MEJOR")
def BusquedaVorazPrimeroElMejor(grafo,inicio,final):
    timepoIncio = time.time()
    costo = 0
    actual = inicio
    minimo = 999
    indiceMinimo = 0
    recorrido = []
    numeroDeNodos = len(grafo[str(actual)])

    # inicializamos el recorrido
    recorrido.append(inicio)

    # como maximo hasta que se llegue a la heuristica
    while int(actual) != int(final):
        minimo = 999999
        numeroDeNodos = len(grafo[str(actual)])
        # para cada nodo del nodo actual
        for i in range(numeroDeNodos):
            # si no es el nodo final
            if int(grafo[str(actual)][i]) != int(final):
                # validamos que la distancia del nodo actual a un nodo adyacente es menor que la distancia minima
                if grafo[str("Distancias."+str(actual))][i] < minimo:
                    # validamos que no lo hayamos escogido
                    if int(grafo[str(actual)][i]) not in recorrido:
                        # cambiamos la distacia minima por la de ese nodo
                        minimo = grafo[str("Distancias."+str(actual))][i]
                        # ahora buscamos en los nodos adyacentes del nodo con la menor distancia
                        indiceMinimo = int(grafo[str(actual)][i])
            else:
                # si es el nodo final, guardamos esa distancia como minima
                minimo = grafo[str("Distancias."+str(actual))][i]
                indiceMinimo = int(grafo[str(actual)][i])
                # finalizamos
                actual = final 
                break
        # ingresamos el nodo minimo a la lista de nodos recorridos
        recorrido.append(int(indiceMinimo))
        # ahora el nodo actual sera el minimo al cual revisaremos sus nodos adyacentes
        actual = indiceMinimo
    # Obtener el costo
    longitudSolucion = len(recorrido)
    for i in range(longitudSolucion-1):
        costo += grafo[str("Distancias."+str(recorrido[i]))][grafo[str(recorrido[i])].index(str(recorrido[i+1]))]
    tiempoFin = time.time()
    print("SOLUCION = "+str(recorrido))
    print("COSTO -> "+str(costo))
    print("TIEMPO DE COMPUTO = "+str(tiempoFin-timepoIncio)+" segundos")


BusquedaVorazPrimeroElMejor(grafo, 2, 5)
