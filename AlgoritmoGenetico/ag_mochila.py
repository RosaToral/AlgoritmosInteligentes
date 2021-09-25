#-*-coding: utf-8 -*-

import random
from copy import deepcopy

#______________________________________________________#
#______________________________________________________#
#                                                      #
#                                                      #
#           Toral Maldonado Rosa Guadalupe             #
#                      2153045948                      #
#                                                      #
#           Análisis y Diseño de algoritmos            #
#   Proyecto final: Aplicación de técnicas heurísticas #
#                   para mejorar la complejidad        #
#                   temporal de un algoritmo:          #
#                                                      #
#           Algoritmo genético en el problema          #
#                     de la mochila                    #
#                                                      #
#                                                      #
#                        martes 23 de julio de 2019    #
#                                                      #
#______________________________________________________#
#______________________________________________________#
#                                                      #

"""
	Variables globales que se van a utilizar a lo largo de todo el programa
	C: capacidad máxima de la mochila
	Arreglo V de volúmenes
	Arreglo B de beneficios
"""
V = []
B = []
C = 0

#Método que lee los beneficios y volúmenes desde un archivo de texto.
#No regresa información
def leerTabla_beneficios_volumenes(NombreArchivo):
	global B
	global V
	global C

	with open(NombreArchivo, 'r') as f:
		for line in f:
			line = line.strip()
			if len(line) > 0:
				B.append(int(line.split()[0]))
				V.append(int(line.split()[1]))

	#El valor de C se ingresa por teclado
	C = int(input("Ingresa el valor de C:\n"))
	print("Volumenes:")
	print(V)
	print("Beneficios:")
	print(B)
	print("\n\n")




"""
	Clase Cromosoma: Representa soluciones al problema de la mochila
		Métodos
			> genera_solucion_aleatoria: genera una solución aleatoria al problema.
										 Regresa un arreglo con la posible solución
			> evalua_fitnes: evalua el volumen que ocupa la solución y su beneficio.
							 No regresa nada
		Atributos
			> cromosoma: arreglo con una posible solución
			> volumen_indv: volumen que consume ese cromosoma
			> beneficio_indv: beneficio que consume ese cromosoma
"""
class Cromosoma(object):
	def __init__(self):
		self.solucion = []
		self.volumen_indv = 0
		self.beneficio_indv = 0

	def genera_solucion_aleatoria(self, B, V, C): #Beneficios y volumenes tienen el mismo tamaño
		n = len(B)
		numero_genes = 0

		while numero_genes < n:
			#Inserta un número random entre 0 y 1 en el arreglo cromosoma
			self.solucion.append(float("{0:.1f}".format(random.uniform(0, 1))))
			if numero_genes == (n-1): #Ya lleno el arreglo
				self.evalua_fitnes(B, V, C) #Evalua el volumen total del 
				if self.volumen_indv > C: #Si el volumen se paso, crea otra solucion
					numero_genes = -1 #Por el incremento de "numero_genes", se pone a -1 
							  #para que pueda regresar a 0
					self.volumen_indv = 0
					del self.solucion[:]
			numero_genes = numero_genes + 1
        
		return self.solucion


	def evalua_fitnes(self, B, V, C):
		#Se ponen a 0, debido a que este algoritmo se usa para seleccionar las soluciones aleatorias
		self.volumen_indv=0
		self.beneficio_indv=0
		n = len(self.solucion)
		i=0

		while i < n:
			self.volumen_indv+=self.solucion[i]*V[i]
			self.beneficio_indv+=self.solucion[i]*B[i]
			i+=1





#Evalúa si se cruza o no a un par de cromosomas al azar según la probabilidad de cruzamiento
#Regresa la cantidad de hijos obtenidos
def cruza_poblacion(seleccionados, probabilidad_cruzamiento):
	num_seleccionados = len(seleccionados)
	hijos_de_cruzamiento = []

	for i in range(num_seleccionados):
		a = 0
		b = 0

	# Dentro del arreglo de cromosomas seleccionados elegimos dos indices diferentes
	while(a == b):
		a = random.randint(0, num_seleccionados-1)
		b = random.randint(0, num_seleccionados-1)

	# Generamos un aleatorio entre 1 y 0 para determinar si se cruzan los cromosomas seleccionados
	r = random.random()
        
	# Si r es menor que Pc (prob. de cruzamiento)  entonces se cruzan
	if r < probabilidad_cruzamiento:
		hijos_de_cruzamiento+=cruzamiento(seleccionados[a], seleccionados[b])
    
	return hijos_de_cruzamiento


#Cruza un par de cromosomas para obtener dos hijos por medio del cruzamiento de punto de corte.
#Regresa a los hijos obtenidos
def cruzamiento(padre1, padre2):
	n = len(padre1.solucion)
	hijo1 = Cromosoma()
	hijo2 = Cromosoma()
	while(True):
		punto_cruce = random.randint(1, n-1) #Para que no escoja el cero
		if(hijo1.volumen_indv>C):
			hijo1.solucion = padre1.solucion[:punto_cruce] + padre2.solucion[punto_cruce:]
			hijo1.evalua_fitnes(B, V, C)
		if hijo1.volumen_indv < C:
			break

	while(True):
		if(hijo2.volumen_indv>C):
			hijo2.solucion = padre2.solucion[:punto_cruce] + padre1.solucion[punto_cruce:]
			hijo2.evalua_fitnes(B, V, C)
		if hijo2.volumen_indv < C:
			break

	return [hijo1, hijo2]            


"""	
	Evalúa si se mutan o no algunos cromosomas según la probabilidad de mutación aumentando algún gen
	escogido al azar.
	Regresa a los hijos generados por las mutaciones
"""
def muta_poblacion(seleccionados, probabilidad_mutacion):
	hijos_de_mutacion = []

	for i in seleccionados:
		r = random.random()
		#Si el número aleatorio es menor a la probabilidad de mutación, ese cromosoma se muta
		if r < probabilidad_mutacion:
			hijo = mutacion(i)
			hijos_de_mutacion.append(hijo)
            
	return hijos_de_mutacion


"""
	Muta a un cromosoma aumentando dos de sus genes que se escojen de manera aleatoria.
	Si el cromosoma mutado tiene un volumen total mayor a C, se cambia por otro
	Regresa al hijo mutado
"""
def mutacion(cromosoma):
	n = len(cromosoma.solucion)
	AUX = deepcopy(cromosoma)

	#Si el cromosoma obtenido de la mutación se pasa del volumen de la mochila, se desecha y se crea otro
	while(True):
		a = 0
		b = 0
		cromosoma = deepcopy(AUX)
		while(a == b):
			a = random.randint(0, n-1)
			b =  random.randint(0, n-1)

		#Si alguno de los genes tiene un 1, se deja tal cual
		if cromosoma.solucion[a] != 1:
			gen = random.uniform(cromosoma.solucion[a], 1)
			cromosoma.solucion[a] = float("{0:.1f}".format(gen))

		if cromosoma.solucion[b] != 1:
			gen = random.uniform(cromosoma.solucion[b], 1)
			cromosoma.solucion[b] = float("{0:.1f}".format(gen))

		cromosoma.evalua_fitnes(B, V, C)
		if cromosoma.volumen_indv < C:
			break

	hijo = Cromosoma()
	hijo.solucion = cromosoma.solucion[:]
	hijo.evalua_fitnes(B, V, C)

	return hijo


#Método que ordena a los cromosomas de mayor a menor beneficio.
#Regresa a los cromosomas ordenados
def quicksort_GA(Poblacion):
	n = len(Poblacion)

	if n <= 1:
		return Poblacion
    
	centro = n//2    
	pivote = Poblacion[centro]
	Poblacion.pop(centro)
	menores = []
	mayores = []

	for i in range(0,n-1):
		if Poblacion[i].beneficio_indv < pivote.beneficio_indv:
			menores.append(Poblacion[i])
		else:
			mayores.append(Poblacion[i])

	menores_ordenados = quicksort_GA(menores)
	mayores_ordenados = quicksort_GA(mayores)
	ordenados = mayores_ordenados+[pivote]+menores_ordenados

	return ordenados


#Método que selecciona a los mejores cromosomas.
#Regresa los seleccionados con mejor beneficio y menor volumen
def selecciona_progenitores(poblacion, porcentaje_seleccionados, num_cromosomas):
	# Ordenamos de menor a mayor longitud los cromosomas
	poblacion_ordenada = quicksort_GA(poblacion)
	num_seleccionados = (porcentaje_seleccionados*num_cromosomas)//100
    
	preseleccionados = []
	# Seleccionamos el porcentaje definido de los mejores cromosomas
	#Se salta de inmediato a todas las soluciones que se pasan del volumen de la mochila
	for i in range(num_seleccionados):
		if poblacion_ordenada[i].volumen_indv < C:
			preseleccionados.append(poblacion_ordenada[i])
    
	# Creamos un excedente para realizar suficientes copias de los seleccionados
	for i in range(5):
		preseleccionados = preseleccionados+preseleccionados
        
	seleccionados = []
    
	# Acotamos los preseleccionados con excedente al numero original de la poblacion
	for i in range(num_cromosomas):
		seleccionados.append(preseleccionados[i])

	return seleccionados


"""
	Método que selecciona a los cromosomas de la siguiente generación manteniendo el número
	original de cromosomas que la población inicial.
	Regresa a los nuevos cromosomas de la nueva población
"""
def reemplazo_poblacion(poblacion, numero_cromosomas):
	nueva_poblacion = []
	for i in range(numero_cromosomas):
		nueva_poblacion.append(poblacion[i])            
	return nueva_poblacion


#Algoritmo genético principal
#No regresa nada
def AG():
	NombreArchivo = 'instancia_mochila_50_obj.txt'
	leerTabla_beneficios_volumenes(NombreArchivo)

	# Parametros a modificar para obtener diferente rendimiento del algoritmo
	numero_cromosomas = 10
	porcentaje_seleccionados = 90
	probabilidad_mutacion = 0.5
	probabilidad_cruzamiento = 0.5

	#Se genera la población inicial
	nueva_poblacion=[] 
	poblacion = []

	for i in range(numero_cromosomas):
		poblacion.append(Cromosoma())    

	#Se evalúan los fitnes de cada cromosoma
	for i in range(numero_cromosomas):
		poblacion[i].genera_solucion_aleatoria(B, V, C)
		poblacion[i].evalua_fitnes(B, V, C)

	#Se ejecuta el algoritmo genético para hacer 50 pruebas
	AUX=poblacion[:]
	for num_generaciones in range(1,50): 
		poblacion=AUX[:]      
		for generacion in range(num_generaciones*100): #Para que vaya crenado generaciones aún más grandes

			seleccionados = selecciona_progenitores(poblacion, porcentaje_seleccionados, numero_cromosomas)
        
			hijos_cruzamiento = cruza_poblacion(seleccionados, probabilidad_cruzamiento)
    
			hijos_mutacion = muta_poblacion(seleccionados, probabilidad_mutacion)
        
			poblacion_temporal = []

			poblacion_temporal = quicksort_GA(seleccionados+hijos_cruzamiento+hijos_mutacion)

			"""
				Se añada al principio de esta lista el mejor elemento de la población
				actual para asegurar que sobreviva a la siguiente generación.
			"""
			poblacion_temporal.insert(0,seleccionados[0])
            
			nueva_poblacion = reemplazo_poblacion(poblacion_temporal, numero_cromosomas)

			#Se imprimen los dos mejores cromosomas de cada generación
			if(generacion == num_generaciones*100-1):
				print('Generacion ',generacion)
				for i in range(len(nueva_poblacion)-1,numero_cromosomas-3,-1):
					# print("({}, {})".format(num_generaciones*100, nueva_poblacion[i].beneficio_indv))
					print("    ",nueva_poblacion[i].solucion)
					print("        Volumen: ", nueva_poblacion[i].volumen_indv)
					print("        Beneficio: ", nueva_poblacion[i].beneficio_indv)

					input()
            
			poblacion = nueva_poblacion[:]

			del nueva_poblacion[:]



# Llamado al algoritmo genetico
AG()