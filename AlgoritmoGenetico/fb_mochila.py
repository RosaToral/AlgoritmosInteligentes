#-*-coding: utf-8 -*-

from random import uniform, random, randint

#______________________________________________________#
#______________________________________________________#
#													   #
#													   #
#			Toral Maldonado Rosa Guadalupe			   #
#			  		   2153045948					   #
#													   #
#			Análisis y Diseño de algoritmos			   #
#	Proyecto final: Aplicación de técnicas heurísticas #
#					para mejorar la complejidad		   #
#					temporal de un algoritmo: 		   #
#													   #
#			Algoritmo genético en el problema		   #
#					  de la mochila					   #
#													   #
#													   #
#						 martes 23 de julio de 2019    #
#													   #
#______________________________________________________#
#______________________________________________________#
#													   #


"""
	Variables globales que se van a utilizar a lo largo de todo el programa
	C: capacidad máxima de la mochila
	Arreglo V de volúmenes
	Arreglo B de beneficios
"""
n = 0
B = []
V = []
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
	Método que crea varias soluciones partiendo de una generada al azar.
	Cambia el valor de una posición en el arreglo inicial al azar y lo 
	guarda en un arreglo de arreglos.
	Regresa un arreglo con todas las soluciones
"""
def crea_soluciones(A):
	soluciones = []
	for x in range(len(A)):
		j = randint(0, n)
		if A[j] == 1.0:
			x-=1
		else:
			#Cambia el valor en la posición seleccionada y guarda la solución.
			aux=A[j]
			A[j] = float("{0:.1f}".format(uniform(A[j], 1)))
			soluciones.append(A[:])
			#Regresa a su valor original.
			A[j]=aux

	return soluciones


"""
	Método que evalúa el volumen total y el beneficio total de cada solución y
	guarda al mejor de todos.
	Regresa la mejor solución obtenida su beneficio y su volumen
"""
def encuentra_mejor_solucion(soluciones, mejor_s, mejor_b, mejor_v):
	for sol in soluciones:
		#pone el volumen y el beneficio de cada arreglo a cero antes de calcularlo
		volumen_indiv = 0
		beneficio_indiv = 0

		for k in range(n): #calcula beneficios y volúmenes
			volumen_indiv+=V[k]*sol[k]
			beneficio_indiv+=B[k]*sol[k]

		#Encuentra al mejor de todos
		if ((volumen_indiv <= C) and (beneficio_indiv > mejor_b)):
			mejor_v = volumen_indiv
			mejor_b = beneficio_indiv
			mejor_s = sol[:]

	return mejor_s, mejor_b, mejor_v


#Método de la mochila por fuerza bruta. Crea 10 solciones de la mejor actual
#Regresa la mejor solución de todas
def problema_mochila_fb(A):
	mejor_beneficio = 0
	mejor_volumen = 0
	soluciones = []
	AUX = A[:]

	for prueba in range(1, 51):
		A = AUX[:]
		print("========================Prueba {}: ========================".format(prueba))
		for i in range(100*prueba): #Crea diferentes soluciones para A
			soluciones = crea_soluciones(A)
			A, mejor_beneficio, mejor_volumen = encuentra_mejor_solucion(soluciones, A, mejor_beneficio, mejor_volumen)

			print("\nMejor solución ({}): ".format(i))
			print("	", A)

			print("			Mejor volumen: ", mejor_volumen)
			print("			Mejor beneficio: ", mejor_beneficio)

			# print("({}, {})".format(prueba*100, mejor_beneficio))
			input()

		#Elimina el contenido de las soluciones para la siguiente prueba
		del soluciones[:]

	return A


#Método principal.
#No regresa nada
def inicio():
	global n
	leerTabla_beneficios_volumenes("instancia_mochila_50_obj.txt")
	n = len(V)

	#Arreglo A inicializado con números aleatorios entre 0 y 1
	A = list(range(n))

	for i in range(0,n):
		A[i] = float("{0:.1f}".format(uniform(0, 0.3)))

	n = n-1

	print("Arreglo inicial: ")
	print(A)
	problema_mochila_fb(A)


#Llamado al método principal
inicio()
	
