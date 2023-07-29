from functools import cache
from math import radians
import random 
import pprint
import time


def inst_ruta_mas_corta(cantidadNodos,conCosto,conDistancia,esConexo):
    print("CREANDO...")
    timepoIncio = time.time()
    numeroNodo = 1
    grafo = {}
    adyacenciaNodoActual = []
    nodosDisponibles = []
    nodosDisponiblestem = []
    costos=[]
    costosTem=[]
    distancia =[]
    distanciasTem=[]
    nodosActualizar = [] #
    distanciasActualizar = [] #
    nodosAgregar = []
    rutas = []
    noCrearGrafo = False
    # Abro el archivo para ver si ya se ha generado algun grafo
    ################# GUARDAMOS #######################
    guardar = open('inst_Grafos.txt', 'r')
    if str(guardar.readline()) != "":
        noCrearGrafo = True
    guardar.close()
    ###################################################
    if noCrearGrafo == False:
        if cantidadNodos >= 2:
            for i in range(cantidadNodos):
                nodosDisponibles.append(str(numeroNodo))
                nodosDisponiblestem.append(str(numeroNodo))
                numeroNodo+=1
            numeroNodo = 1
            for j in range(cantidadNodos):# creamos el grafo
                if esConexo == True:
                    cantidadAdyacentes = 10
                else:
                    cantidadAdyacentes = random.randint(1,int(cantidadNodos/2)) # decidimos aleatoriamente a cuantos nodos tendra adyacentes     
                nodosAEscoger=0

                while nodosAEscoger < cantidadAdyacentes:
                    elegido = random.randint(0,len(nodosDisponiblestem)-1)      # decidimos aleatoriamente a que nodo se conectara
                    if nodosDisponiblestem[elegido] != nodosDisponibles[j]:# bloqueamos que se eliga a si mismo el nodo actual
                        if int(nodosDisponibles[j]) < int(nodosDisponiblestem[elegido]):    # acomodamos en orden la ruta 
                            rutaGuardada = nodosDisponibles[j]+nodosDisponiblestem[elegido]
                        else:
                            rutaGuardada = nodosDisponiblestem[elegido]+nodosDisponibles[j]
                        # busco si la ruta ya existe
                        if conCosto == True or conDistancia == True:
                            rutas.append(rutaGuardada)
                            if rutas.count(rutaGuardada) == 1:  # Noexiste                
                                if conCosto == True:
                                    c = random.randint(1, 10)
                                    costos.append(c)
                                    costosTem.append(c)
                                if conDistancia == True:
                                    d = random.randint(2, 30)
                                    distancia.append(d)
                                    distanciasTem.append(d)
                            else: # Existe
                                if conCosto == True:   
                                    costos.append(costos[rutas.index(rutaGuardada)])
                                    costosTem.append(costos[rutas.index(rutaGuardada)])
                                if conDistancia == True:
                                    distancia.append(distancia[rutas.index(rutaGuardada)])
                                    distanciasTem.append(distancia[rutas.index(rutaGuardada)])
                        adyacenciaNodoActual.append(nodosDisponiblestem[elegido]) # lo guardamos en una lista            
                        nodosDisponiblestem.pop(elegido)  # eliminamos    
                        nodosAEscoger += 1
                    else:
                        nodosDisponiblestem.pop(elegido)  # eliminamos                
                nodosDisponiblestem = nodosDisponibles.copy()
                grafo.setdefault(nodosDisponibles[j], adyacenciaNodoActual)
                if conCosto == True:
                    grafo.setdefault(str("Costos....."+str(nodosDisponibles[j])),costosTem)
                if conDistancia == True:
                    grafo.setdefault(str("Distancias."+str(nodosDisponibles[j])), distanciasTem)
                distanciasTem = []
                costosTem = []
                adyacenciaNodoActual = []
            print("AJUSTANDO...")
            ################# AJUSTAMOS EL GRAFO PARA QUE SEA COMPLETO ###################
            for f in range(1,cantidadNodos+1): # para cada nodo
                #print("NODO "+str(f)+ " -> "+str(grafo[str(f)]))
                for k in range(  len( grafo[str(f)] )  ): # puede empezar en 0
                    try: 
                        # lista del nodoactual | un nodo de esa lista | el nodo padre |
                        pos = grafo[str(grafo[str(f)][k])].index(str(f))
                    except:
                        distanciasActualizar = []
                        nodosActualizar = []                     #  Esto es un numero  #
                        #print("NODO "+str(f)+ " falta en NODO "+ str(grafo[str(f)][k]))
                        nodosActualizar = grafo[str( grafo[ str(f) ][k] )] #---------------
                        nodosActualizar.append(str(f))
                        
                        # ahora le doy una distancia
                        # guardo la ruta
                        if int(f) > int(grafo[str(f)][k]):
                            rutaGuardada = str(grafo[str(f)][k])+str(f)
                        else:
                            rutaGuardada = str(f)+str(grafo[str(f)][k])
                        rutas.append(rutaGuardada)
                        # busco si la ruta ya existe
                        if rutas.count(rutaGuardada) == 1:  # Noexiste
                            d = random.randint(2, 30)
                            distancia.append(d)
                        else:  # Existe
                            distancia.append(distancia[rutas.index(rutaGuardada)]) 
                            dis = distancia[rutas.index(rutaGuardada)]
                        # buscamos las distancias del nodo al que vamos actualizar
                        distanciasActualizar = grafo[ str("Distancias."+str(grafo[str(f)][k])) ]
                        distanciasActualizar.append(dis)
                        grafo.update({str(grafo[str(f)][k]): nodosActualizar})
                        grafo.update({grafo[str("Distancias."+str(f))][k]: distanciasActualizar})
                        try:
                            grafo.pop(int(grafo[str("Distancias."+str(f))][k]))
                        except:
                            print("NO ELIMINE NADA")
            tiempoFin = time.time()
            print("TIEMPO DE COMPUTO = "+str(tiempoFin-timepoIncio)+" segundos")
            ################# GUARDAMOS #######################
            guardar = open('inst_Grafos.txt', 'a')
            for key in grafo:
                #guardar.write(str(str(key)+'\n'))
                guardar.write(str(str(grafo[key])))
                guardar.write('\n')
            guardar.close()
            ###################################################
            return grafo
        else:
            print("La cantidad de nodos debe ser mayor o igual a 2")
        return grafo
    else: 
        print("UN GRAFO YA HA SIDO CREADO")

inst_ruta_mas_corta(20, False, True, True)

xd = input("PRESIONE CUALQUIER TECLA PARA TERMINAR...")
