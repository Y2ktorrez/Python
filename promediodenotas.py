#Funcion que devuelve el promedio de notas de entre las notas de todos los argumentos 

from typing_extensions import runtime


def promedio(a, b) : 
    return a + b / 2 
print(promedio(30,20))
def promedio(a, b, c) : 
    return a + b + c / 3 

def promedio(a, b, c, d) : 
    return a + b + c + d / 4

def promedio(a, b, c, d, e) : 
    return a + b + c + d + e / 5

#Funcion que devuleve la peor nota de entre las notas de todos los argumentos 

def menorNota(a, b) : 
    if a < b : return a 
    else : return b 

def menorNota(a, b, c) : 
    if a < b & a < c : return a 
    if b < a & b < c : return b 
    else : return c

def menorNota(a, b, c, d) : 
    if a < b & a < c & a < d : return a 
    if b < a & b < c & b < d : return b 
    if c < a & c < b & c < d : return c 
    else : return d

def menorNota(a, b, c, d, e) : 
    if a < b & a < c & a < d & a < e : return a
    if b < a & b < c & b < d & b < e : return b 
    if c < a & c < b & c < d & c < e : return c
    if d < a & d < b & d < c & d < e : return d
    else : return e 

#Funcion que devuelve el promedio de las dos mejores notas 

def notFinal(a , b) : 
    return a + b / 2 

def notFinal(a, b, c) : 
    return mayor(a, b, c) + segMayor(a, b, c) / 2 

def notFinal(a, b, c, d) : 
    return mayor(a, b, c, d) + segMayor(a, b, c, d) / 2

def notFinal(a, b, c, d, e) : 
    return mayor(a, b, c, d, e) + segMayor(a, b, c, d, e) / 2

#Funcion que devuelve el promedio de notas de entre la mayor y peor nota 

def notaProm(a, b) : 
    return a + b / 2

def notaProm(a, b, c) : 
    return mayor(a, b, c) + menor(a. b, c) / 2

def notaProm(a, b, c, d) : 
    return mayor(a, b, c, d) + menor(a, b, c, d) / 2

def notaProm(a, b, c, d, e) : 
    return mayor(a, b, c, d, e) + menor(a, b, c, d, e) / 2

#Funcion que devuelve la nota ponderada de las tres mejores notas, donde la mayor nota
#vale 50%, la segunda nota vale el 30% y la tercera nota el 20% 

def notaPonderado(a, b, c) : 
    return (mayor(a, b, c) * 50) /100 + (segMayor(a, b, c) * 30) / 100 * ()