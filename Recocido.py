from numpy import append
import random
import math
import time

grafo = {}

# obtenemos el grafo guardado
guardar = open('inst_Grafos.txt', 'r')
for i in range(20): # EL NUMERO SE CAMBIA SERGUN LA CANTIDAD DE NODOS
    xd = grafo.setdefault(str(i+1), eval(guardar.readline()))
    xd = grafo.setdefault(str("Distancias."+str(i+1)), eval(guardar.readline()))
guardar.close()

def generarVecinoAleatorio(incial,final):  
    elegido = 0
    visitados = [0] # Para evitar el error del len()
    camino = []
    posibles = []
    cantidadPosibles = 0
    actual = incial
    visitados.append(actual)
    camino.append(actual)
    while actual != final:
        # Introdusco a una lista todos los nodos adyacentes del nodo actual que no esten en la lista de visitados
        posibles = []   
        cantidadPosibles = 0            
        for i in range( len( grafo[ str(actual) ]  )   ):
            enVisitado = False
            for j in range(len(visitados)):
                # Comparo si el nodo adyacente esta en la lista de visitados
                if int(grafo[str(actual)][i]) == int(visitados[j]):
                    enVisitado = True
            if enVisitado == False:
                posibles.append(int(grafo[str(actual)][i]))
                cantidadPosibles +=1       
        # Si hay mas de un nodo posible a elegir
        if cantidadPosibles != 0:
            if cantidadPosibles > 1:
                # Escogo un nodo en la lista de posibles
                elegido = random.randint(0,cantidadPosibles-1)
            else:
                elegido = 0  # Porque solo hay una opcion
            # El elegido lo ingreso a los visitados
            visitados.append(int(posibles[elegido]))
            # Ahora el elegido es el actual
            actual = int(posibles[elegido])
            # Y lo ingreso al camino
            camino.append(int(actual))
        else: # No hay nodos posibles porque todos ya han sido visitados
            # Si el nodo actual no tiene nodos adyacentes sin visitar
            # Lo sacamos del camino
            camino.pop()
            # Y el actual es el ultimo en la lista de camino
            actual = int(camino[len(camino)-1])
    return camino               
def evaluarVecino(vecino):
    # Para cada nodo en vecinos
    valor = 0
    posicion = 0
    for nodo in vecino:
        posicion += 1
        if int(len(vecino)) != int(posicion):
            #print("NODO PADRE -> "+str(nodo)+" NODO SIGUEINTE -> "+str(vecino[posicion]))
            #             |          NODO PADRE             |                NODO SIGUIENTE              |   
            valor += grafo[  str("Distancias."+str(nodo))  ][grafo[str(nodo)].index(str(vecino[posicion]))]
    return valor 


# Algoritmo Recocido simulado 
def recocidoSimulado():
    incio = time.time()
    solucionActual = []
    vecino = []
    valorActual = 0
    valorVecino = 0
    valorFinal = 0
    vecinoFinal = []
    temperaturaInicial = 0
    temperaturaFinal = 0
    velocidadDeEnfriamiento = 0
    iteracionesTotales = 0
    iteracion = 0
    iteracionesMaximas = 0
    rn = 0.1 # valor aleatorio 
    # creo una solucion incial
    solucionActual = generarVecinoAleatorio(2, 5) # -----------
    valorActual = evaluarVecino(solucionActual)
    # inicializo la tempertura
    temperaturaInicial = 50
    temperaturaFinal = 30 
    iteracionesMaximas = 100
    velocidadDeEnfriamiento = 1 # cada iteracion
    # entro al ciclo
    while temperaturaInicial > temperaturaFinal:
        # valido si la iteracion es menor a la velocidad de enfriamiento
        if iteracion <= iteracionesMaximas:
            # generamos un nuevo vecino
            vecino = generarVecinoAleatorio(2,5) # ------------
            valorVecino = evaluarVecino(vecino)
            # comparo el valor del vecino con el valor actual
            if valorVecino < valorActual:
                #print(str(valorVecino)+"<"+str(valorActual))
                # reemplazo el valor mejor y lo comviento en valor actual
                valorActual = valorVecino
                valorFinal = valorVecino
                vecinoFinal = vecino
            else:
                # no es mejor la solucion del nuevo vecino
                # calculo una probabilidad
                # resto la solucion actual menos la nueva del vecino generado
                diferenciaValores = valorActual-valorVecino
                # ingreso ese valor a la formula
                fraccion = (diferenciaValores/temperaturaInicial)*-1
                e = math.e
                pr = e**fraccion
                # si la probabilidad es mayor a la probabilidad que definimos
                if pr < rn:
                    # nos quedamos con el nuevo valor del vecino
                    valorActual = valorVecino
        else:
            # si la iteracion es igual o mayor a la velocidad de enfriamiento
            # disminuyo la temperatura
            temperaturaInicial = temperaturaInicial - velocidadDeEnfriamiento

        iteracion+=1
        iteracionesTotales+=1
    # solucion final
    print("SOLUCION = "+str(vecinoFinal))
    print("COSTO = "+ str(valorFinal))
    fin = time.time()
    print("TIEMPO DE COMPUTO = "+ str(fin - incio)+" segundos")
    print("")

print("ALGORITMO RECOCIDO SIMULADO")

recocidoSimulado()

xd = input("PRESIONE CUALQUIER TECLA PARA TERMINAR")
