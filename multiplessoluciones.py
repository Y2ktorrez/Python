#sumaEnteros( n )  : Función que devuelve la suma de los primeros n-números enteros positivos.
#Ej. Si n = 5, sum = 1 + 2 + 3 + 4 + 5

def sumaN(n) :
	c = 1
	sum = 0 
	while (c <= n):
		sum = sum + c
		c = c + 1
	return sum 


#sumaEnteros(a, b) : Función que devuelve la suma de los enteros de a hasta b.
#Ej. Si a = 10, b = 15, sum = 10 + 11 + 12 + 13 + 14 + 15

def sumaAB(a, b) :
	c = 1 
	sum = 0
	v = a
	while (c <= (b + 1) - a):
		sum = sum + v 
		v = v + 1
		c = c + 1
	return sum 

#sumaPares( n ) : Función que devuelve la suma de los primeros n números enteros positivos.
#Ej. Si n = 4, sum = 2 + 4 + 6 + 8

def sumaPares(n) : 
	c = 1
	sum = 0
	v = 0
	while (c <= n):
		v = v + 2
		sum = sum + v
		c = c + 1 
	return sum 

#sumaPares( n ) : Función que devuelve la suma de los primeros n números enteros positivos.
#Ej. Si n = 4, sum = 2 + 4 + 6 + 8

def sumaImpares(n) : 
	c = 1 
	sum = 0 
	v = -1
	while (c <= n):
		v = v + 2
		sum = sum + v
		c = c + 1
	return sum 

#sumaTramos(a, k, n) : Función que devuelve la sumatoria de los primeros n-números a partir de a, incrementados de k en k.
#Ej. Si n = 5, a = 10, k = 4, sum = 10, 14, 18, 22, 26

def sumaTramos(n, a, k) :
	c = 1 
	sum = 0
	while (c <= n):
		sum = sum + a
		a = a + k
		c = c + 1
	return sum 
print(sumaTramos(5, 10, 4))
#sumaProd( n ) : Función que devuelve la sumatoria de los primeros n productos con factores crecientes y decrecientes.
#Ej. Si n = 5, sum = 1*5 + 2*4 + 3*3 + 4*2 + 5*1

def sumaProd(n) :
	c = 1 
	sum = 0 
	v = n
	while (c <= n):
		sum = sum + v*c
		v = v - 1
		c = c + 1
	return sum 

#sumaAlterna( n ) : Función que devuelve la sumatoria de los primeros n enteros, con sumas y restas alternativamente.
#Ej. Si n = 4, suma = 1 - 2 + 3 - 4 + 5

def sumaAlterna(n) :
	i = 1 
	sum = 0 
	b = True
	while (i <= n):
		if (b == True):
			sum = sum + i
			b = False
		else:
			sum = sum + (i * -1)
			b = True
		i = i + 1
	return sum 

#Funciones adicionales
#Funcion que devuelve la suma de los primeros n numeros enteros 

def multPares(n) :
	c = 1 
	mult = 1 
	v = 0 
	while (c <= n):
		v = v + 2
		mult = mult * v
		c = c + 1
	return mult 

#Funcion que devuelve la multiplicacion de los primeros n numeros enteros positivos

def multEnteros(n) :
	c = 1 
	mult = 1
	while (c <= n):
		mult = mult * c
		c = c + 1
	return mult 

#Funcion que devuelve la resta de los primero n numeros enteros positivos 

def restaN(n) :
	c = 1 
	rest = -1
	while (c <= n -1):
		c = c + 1
		rest = rest - c
	return rest 

#Funcion que devuelve la resta de los primeros n numeros entero positivos empezando por el valor mas alto

def restaInv(n) : 
	c = 1 
	rest = n 
	v = n
	while (c <= n):
		v = v - 1
		rest = rest - v
		c = c + 1
	return rest 

#Funcion que devuelve la multiplicacion de los primeros n numeros enteros impares 

def multImpares(n) :
	c = 1 
	mult = 1 
	v = -1
	while (c <= n):
		v = v + 2
		mult = mult * v
		c = c + 1
	return mult 
