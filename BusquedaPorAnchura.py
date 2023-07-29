import time

grafo = {}
grafoAdaptado = {}

# Obtenemos el grafo guardado
guardar = open('inst_Grafos.txt', 'r')
for i in range(20):  # EL NUMERO SE CAMBIA SERGUN LA CANTIDAD DE NODOS
    xd = grafo.setdefault(str(i+1), eval(guardar.readline()))
    # Para reutilizar el codigo de una tarea anterior, creo un grafo adaptado para el
    grafoAdaptado[str(i+1)] = xd
    xd = grafo.setdefault(str("Distancias."+str(i+1)),eval(guardar.readline()))
guardar.close()
print("ESTRATEGIA PRIMERO POR ANCHURA")
# ALGORITMO DE BUSQUEDA POR AMPLITUD
def busquedaPorAmplitud(nodoInicial, nodoFinal):
    timepoIncio = time.time()
    nodoActual = ""
    nodosRecorridos = []
    antecesorNodosRecorridos = []
    solucion = []
    noExiste = True
    encontrado = False
    posNodoActual = 0
    costo = 0
    # Incializamos el nodo actual
    nodoActual = str(nodoInicial)

    # Lo marcamos como visitado
    #                       NODO VISITADO
    nodosRecorridos.append(int(nodoActual))
    #                       NODO ANTECESOR
    antecesorNodosRecorridos.append(0)

    # Mientras no encuentre el nodo final no se acabra el ciclo
    while int(nodoFinal) != int(nodoActual):
        # INCIO DEL ALGORITMO BUSQUEDA POR ANCHURA -------------------------------------------
        # Al inicio el nodoActual es el nodoInicial
        for i in range(len(grafoAdaptado[str(nodoActual)])):

            # Si aun no lo he encontrado
            if encontrado == False:
                # Valido que no lo haya recorrido anteriormente
                noExiste = True
                for k in range(len(nodosRecorridos)):
                    if grafoAdaptado[str(nodoActual)][i] == nodosRecorridos[k]:
                        noExiste = False

            # Si no exisite y si aun no lo hemos encontrado, lo ingreso a la lista de recorridos
            if noExiste == True and encontrado == False:
                # Visito todos los hijos del nodo actual
                nodosRecorridos.append(int(grafoAdaptado[str(nodoActual)][i]))
                antecesorNodosRecorridos.append(int(nodoActual))
                # Valido si ya encontre el nodo final
                if int(grafoAdaptado[str(nodoActual)][i]) == int(nodoFinal):
                    nodoActual = nodoFinal
                    encontrado = True

        # Buscamos la posicion del nodo actual + 1, NOTA: nodoActual es un str, lo conviento a int
        posNodoActual = nodosRecorridos.index(int(nodoActual))

        # Ahora el nodo actual sera el valor de la posicion del nodo actual +1
        if posNodoActual+1 < len(nodosRecorridos):
            nodoActual = nodosRecorridos[posNodoActual+1]
        else:  # Si pasa el ultimo nodo, termina el algoritmo
            nodoActual = nodoFinal

    # FIN DEL ALGORITMO BUSQUEDA POR ANCHURA -------------------------------------------

    


    #print("ESTRATEGIA PRIMERO POR ANCHURA")
    #print("RECORRIDO "+str(nodosRecorridos))
    # ACOMODAR LA SOLUCION
    temporal = int(nodoFinal)
    solucion.append(temporal)
    while temporal != int(nodoInicial):
        solucion.append(
            int(antecesorNodosRecorridos[nodosRecorridos.index(temporal)]))
        temporal = antecesorNodosRecorridos[nodosRecorridos.index(temporal)]
    solucion.reverse()
    print("SOLUCION = "+ str(solucion))

    # Obtener el costo
    longitudSolucion = len(solucion)
    for i in range(longitudSolucion-1):
        costo += grafo[str("Distancias."+str(solucion[i]))][grafo[str(solucion[i])].index(str(solucion[i+1]))]
        #print(grafo[str("Distancias."+str(solucion[i]))][grafo[str(solucion[i])].index(str(solucion[i+1]))])
    print("COSTO =  " + str(costo))
    tiempoFin = time.time()
    print("TIEMPO DE COMPUTO = "+str(tiempoFin-timepoIncio)+" segundos")
    return solucion


busquedaPorAmplitud(2,5)
