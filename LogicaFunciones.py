//Logica 1 utilizando variable auxiliar

#Funcion que devuelve el menor de entre a,b,c,d y e. 

def menorAux(a, b) :
    menor = a 
    if  b < menor: menor = b
    return menor 
print(menorAux(1,2))

def menorAux(a, b, c) :
    menor = a
    if b < menor: menor = b
    if c < menor: menor = c 
    return menor 


def menorAux(a, b, c, d) : 
    menor = a
    if b < menor: menor = b
    if c < menor: menor = c
    if d < menor: menor = d 
    return menor 

def menorAux(a, b, c, d, e) : 
    menor = a 
    if b < menor: menor = b 
    if c < menor: menor = c
    if d < menor: menor = d 
    if e < menor: menor = e 
    return menor 

#Funcion que devuelve el mayor de entre a,b,c,d y e. 

def mayorAux(a, b) :
    mayor = a 
    if  b < mayor: mayor = b
    return mayor 


def mayorAux(a, b, c) :
    mayor = a
    if b < mayor: mayor = b
    if c < mayor: mayor = c 
    return mayor 


def mayorAux(a, b, c, d) : 
    mayor = a
    if b < mayor: mayor = b
    if c < mayor: mayor = c
    if d < mayor: mayor = d 
    return mayor 

def meyorAux(a, b, c, d, e) : 
    mayor = a 
    if b < mayor: mayor = b 
    if c < mayor: mayor = c
    if d < mayor: mayor = d 
    if e < mayor: mayor = e 
    return mayor  


//Logica 2 Utilizando Operadores Logicos 

#Funcion que devuelve el menor de entre a, b, c, d y e. 

def menorAnd(a, b) : 
    if a < b : return a
    return b 

def menorAnd(a, b, c) : 
    if a < b & a < c : return a 
    if b < a & b < c : return b 
    return c

def menorAnd(a, b, c, d) : 
    if a < b & a < c & a < d : return a
    if b < a & b < c & b < c : return b
    if c < a & c < b & c < d : return c 
    return d 

def menorAnd(a, b, c, d, e) : 
    if a < b & a < c & a < d & a < e : return a 
    if b < a & b < c & b < d & b < e : return b
    if c < a & c < b & c < d & c < e : return c
    if d < a & d < b & d < c & d < e : return d
    return e

#Funcion que devuelve el mayor de entre a,b,c,d y e. 

def mayorAnd(a, b) : 
    if a > b : return a
    return b 

def mayorAnd(a, b, c) : 
    if a > b & a > c : return a 
    if b > a & b > c : return b 
    return c

def mayorAnd(a, b, c, d) : 
    if a > b & a > c & a > d : return a
    if b > a & b > c & b > c : return b
    if c > a & c > b & c > d : return c 
    return d 

def mayorAnd(a, b, c, d, e) : 
    if a > b & a > c & a > d & a > e : return a 
    if b > a & b > c & b > d & b > e : return b
    if c > a & c > b & c > d & c > e : return c
    if d > a & d > b & d > c & d > e : return d
    return e


//Logica 3 Utilizando Llamadas a otras funciones 

#Funciones que devuelve el menor de entre a, b, c, d y e 

def menor(a, b) : 
    if a < b : return a 
    return b 

def menor(a, b, c) : 
    return menor(menor(a, b), c)

def menor(a, b, c, d) : 
    return menor(menor(a, b, c), d)

def menor(a, b, c, d, e) : 
    return menor(menor(a, b, c, d), e)

#Funciones que devuelce el mayor de entre a, b, c, d y e 

def mayor(a, b) : 
    if a > b : return a 
    return b 

def mayor(a, b, c) : 
    return mayor(mayor(a, b), c)

def mayor(a, b, c, d) :
    return mayor(mayor(a, b, c), d)

def mayor(a, b, c, d, e) : 
    return mayor(mayor(a, b, c, d), e)


//Logicas para encontrar el segundo menor y el segundo mayor 

#Funcion que devuelve el segundo menor entre a, b, c, d y e. 

def segMenor(a, b) : 
    men = a
    if a == men : return b 
    return a 

def segMenor(a, b, c) : 
    men = menor(a, b, c)
    if a == men : return menor(b, c)
    if b == men : return menor(a, c)
    return menor(a, b)

def segMenor(a, b, c, d) : 
    men = menor(a, b, c, d)
    if a == men : return menor(b, c, d)
    if b == men : return menor(a, c, d)
    if c == men : return menor(a, b, d)
    return menor(a, b, c)

def segMenor(a, b, c, d, e) : 
    men = menor(a, b, c, d, e)
    if a == men : return menor(b, c, d, e)
    if b == men : return menor(a, c, d, e)
    if c == men : return menor(a, b, d, e)
    if d == men : return menor(a, b, c, e)
    return menor(a, b, c, d)

#Funcion que devuelve el segundo mayor de entre a, b, c, d y e 

def segMayor(a, b) : 
    may = a 
    if a == may : return a 
    return b 

def segMayor(a, b, c) : 
    may = mayor(a, b, c)
    if a == may : return mayor(b, c)
    if b == may : return mayor(a, c)
    return mayor(a, b)

def segMayor(a, b, c, d) : 
    may = mayor(a, b, c, d)
    if a == may : return mayor(b, c, d)
    if b == may : return mayor(a , c, d)
    if c == may : return mayor(a, b, d)
    return mayor(a, b, c)

def segMayor(a, b, c, d, e) : 
    may = mayor(a, b, c, d, e)
    if a == may : return mayor(b, c, d, e)
    if b == may : return mayor(a, c, d, e)
    if c == may : return mayor(a, b, d, e)
    if d == may : return mayor(a, b, c, e)
    return mayor(a, b, c, d)

#Funcion que devuelve el tercer menor de entre a, b, c, d y e

def tercerMenor(a, b, c) :
    tercer = mayorAux(a, b, c)
    return tercer 

def tercerMenor(a, b, c, d) : 
    tercer = segMenor(a, b, c, d)
    if a == tercer : return segMenor(b, c, d)
    if b == tercer : return segMenor(a, c, d)
    if c == tercer : return segMenor(a, b, d)
    return segMenor(a, b, c)

def tercerMenor(a, b, c, d, e) : 
    tercer = segMenor(a, b, c, d, e)
    if a == tercer : return segMenor(b, c, d, e)
    if b == tercer : return segMenor(a, c, d, e)
    if c == tercer : return segMenor(a, b, d, e)
    if d == tercer : return segMenor(a, b, c, e)
    return segMenor(a, b, c, d)
    
#Funcion que devuelve el tercer mayor de entre a, b, c, d y e 

def tercerMayor(a, b, c) : 
    tercer = menor(a, b, c)
    return tercer

def tercerMayor(a, b, c, d) : 
    tercer = segMayor(a, b, c, d)
    if a == tercer : return segMayor(b, c, d)
    if b == tercer : return segMayor(a, c, d)
    if c == tercer : return segMayor(a, b, d)
    return segMayor(a, b, c)

def tercerMayor(a, b, c, d, e) :
    tercer = segMayor(a, b, c, d, e)
    if a == tercer : return segMayor(b, c, d, e)
    if b == tercer : return segMayor(a, c, d, e)
    if c == tercer : return segMayor(a, b, d, e)
    if d == tercer : return segMayor(a, b, c, e)
    return segMayor(a, b, c, d)