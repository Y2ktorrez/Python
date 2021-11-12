#Funcion logica que devuelve True, si a es un numero impar. 

def impar(a) :
    return a % 2 != 0

#Funcion logica que devuelve True, si a es un numero par. 

def par(a) :
    return a % 2 == 0

#Función lógica que devuelve True, si entre los argumentos solo dos son pares
#las otras pares.

def dosPares(a, b) :
    return par(a) and par(b)

def dosPares1(a, b, c) : 
    return dosPares(a, b) and impar(c) or dosPares(a, c) and impar(b) or dosPares(b, c) and impar(a)               

def dosPares(a, b, c, d) : 
    return dosPares(a, b) and impar(c, d) or dosPares(a, c) and impar (b, d) or dosPares(a, d) and impar(b, c) or dosPares(b , c) and impar(a, d) or dosPares(b, d) and impar(a, c) or dosPares(c, d) and impar(a, b)

def dosPares(a, b, c, d, e) : 
    return dosPares( a, b )  and  impar( c, d, e ) or dosPares( a, c )  and  impar( b, d, e ) or dosPares( a, d )  and  impar( b, c, e ) or dosPares( a, e )  and  impar( b, c, d ) or dosPares( b, c )  and  impar( a, d, e ) or dosPares( b, d )  and  impar( a, c, e ) or dosPares( b, e )  and  impar( a, c, d ) or dosPares( c, d )  and  impar( a, b, e ) or dosPares( c, e )  and  impar( a, b, d ) or dosPares( d, e )  and  impar( a, b, c ) 

#Función Lógica que devuelve True, si tres argumentos son pares y las otras impares

def tresPares(a, b, c) : 
    return par(a) and par(b) and par (c)

def tresPares1(a, b, c, d) : 
    return tresPares(a, b, c) and impar(d) or tresPares(a, b, d) and impar(c) or tresPares(a, c, d) and impar(b) or tresPares(b, c, d) and impar(a)

def tresPares(a, b, c, d, e) : 
    return tresPares( a, b, c )  and  impar( d, e ) or tresPares(a, b, d)  and  impar(c, e) or tresPares(a, b, e)  and  impar(c, d) or tresPares(a, c, d)  and  impar(b, e) or tresPares(a, c, e)  and  impar(b, d) or tresPares(a, d, e)  and  impar(b, c) or tresPares(b, c, d)  and  impar(a, e) or tresPares(b, c, e)  and  impar(a, d) or tresPares(b, d, e)  and  impar(a, c) or tresPares(c, d, e)  and  impar(a, b)     
    
#Función lógica que devuelve True, si de entre todos los argumentos existe al menos un argumento par.

def existePar(a, b) : 
    return par(a) or par(b)

def existePar(a, b, c) : 
    return par(a) or par(b) or par(c)

def existePar(a, b, c, d) : 
    return par(a) or par(b) or par(c) or par(d)

def existePar(a, b, c, d, e) :
    return par(a) or par(b) or par(c) or par(d) or par(e)

#Función lógica que devuelve True, si de entre todos los argumentos existe al menos un argumento impar.

def existeImpar(a, b) : 
    return impar(a) or impar(b)

def existeImpar(a, b, c) : 
    return impar(a) or impar(b) or impar(c)

def exiteImpar(a, b, c, d) :
    return impar(a) or impar(b) or impar(c) or impar(d) 

def exiteImpar(a, b, c, d, e) : 
    return impar(a) or impar(b) or impar(c) or impar(d) or impar(e)

# Función lógica que devuelve True, si todos los argumentos son pares.

def todosPares(a, b) : 
    return par(a) and par(b) 

def todosPares(a, b, c) : 
    return par(a) and par(b) and par(c)

def todosPares(a, b, c, d) : 
    return par(a) and par(b) and par(c) and par(d)

def todosPares(a, b, c, d, e) : 
    return par(a) and par(b) and par(c) and par(d) and par(e)

#Función lógica que devuelve True, si todos los argumentos son impares.

def todosImpares(a, b) : 
    return impar(a) and impar(b)

def todosImpares(a, b, c) : 
    return impar(a) and impar(b) and impar(c)

def todosImpares(a, b, c, d) : 
    return impar(a) and impar(b) and impar(c) and impar(d)

def todosImpares(a, b, c, d, e) : 
    return impar(a) and impar(b) and impar(c) and impar(d) and impar(e)

#Función lógica que devuelve True, si existe al menos un par y al menos un impar de entre sus argumentos de la función.

def parImpar(a, b) : 
    return par(a) and impar(b) or impar(a) and par(b)

def parImpar(a, b, c) : 
    return par(a) and existeImpar(b, c) or par(b) and existeImpar(a, c) or par(c)  and  existeImpar(a, b)

def parImpar(a, b, c, d) : 
    return par(a) and existeImpar(b, c, d) or par(b) and existeImpar(a, c, d) or par(c) and existeImpar(a, b, d) or par(d) and existeImpar(a, b, c)     

def parImpar(a, b, c, d, e) : 
    par(a) and existeImpar(b, c, d, e) or par(b) and existeImpar(a, c, d, e) or par(c) and existeImpar(a, b, d, e) or par(d) and existeImpar(a, b, c, e) or par(e) and existeImpar(a, b, c, d) 

#Función lógica que devuelve True, si la secuencia de argumentos se alternan de pares e impares. No pueden haber dos argumentos juntos pares o impares.

def alterno(a, b) : 
    return par(a) and impar(b) or impar(a) and par(b)

def alterno(a, b, c) : 
    return par(a) and impar(b) and par(c) or impar(a) and par(b) and impar(c)

def alterno(a, b, c, d) : 
    return par(a) and impar(b) and par(c) and impar(d) or impar(a) and par(b) and impar(c) and par(d)

def alterno(a, b, c, d, e) : 
    return par(a) and impar(b) and par(c) and impar(d) and par(e) or impar(a) and par(b) and impar(c) and par(d) and impar(e)

#Función lógica que devuelve True, si todos los argumentos son iguales. Sugerencia, expresar en función de los predicados anteriores.

def iguales1(a, b) : 
    return a == b 

def iguales2(a, b, c) :
    return a == b and b == c

def iguales3(a, b, c, d) :
    return a == b and b == c and  c == d 

def iguales4(a, b, c, d, e) : 
    return a == b and b == c and c == d and d == e

#Función lógica que devuelve True, si todos los argumentos son diferentes.

def diferentes1(a, b) : 
    return a != b

def diferentes2(a, b, c) :
    return a != b and b != c 

def diferentes3(a, b, c, d) :
    return a != b and b != c and c != d

def diferentes4(a, b, c, d, e) : 
    return a != b and b != c and c != d and d != e

#Función lógica que devuelve True, si existen dos argumentos iguales y los otros argumentos diferentes entre ellos y diferentes a los dos iguales.

def dosIguales1(a, b) : 
    return a == b 

def dosIguales2(a, b, c) : 
    return a == b and a != c or a == c and a != b or b == c and b != a

def dosIguales3(a, b, c, d) : 
    return a == b and a != c and c != d or a == c and a != b and b != d or a == d and a != b and b != c or b == c and b != a and a != d or b == d and b != a and a != c or c == d and c != a and a != b

def dosIguales4(a, b, c, d, e) : 
    return a == b and a != c and c != d and c != e and d != e or a == c and a != b and b != d and b != e and d != e or a == d and a != b and b != c and b != e and c != e or a == e and a != b and b != c and b != d and c != d or b == c and b != a and a != d and a != e and d != e or b == d and b != a and a != c and a != e and c != e or b == e and b != a and a != c and a != d and c != d or c == d and c != a and a != b and a != e and b != e or c == e and c != a and a != b and a != d and b != d or d == e and d != a and a != b and a != c and b != c 

# Función lógica que devuelve True, si existen tres argumentos iguales y los otros argumentos diferentes entre ellos y diferentes a los tres iguales.

def tresIguales1(a, b, c) : 
    return a == b and a == c

def tresIguales2(a, b, c, d) : 
    return a == b and a == c and a != d or a == b and a == d and a != c or a == c and a == d and a != b or b == c and b == d and b != a  

def tresIguales3(a, b, c, d, e) : 
    return a == b and a == c and a != d and a != e or a == b and a == d and a != c and a != e or a == c and a == d and a != b and a != e or a == c and a == e and a != b and b != d or a == b and a == e and a != c and c != d or a == c and a == e and a != b and b != d or a == d and a == e and a != b and b != c or b == c and b == d and b != a and a != e or b == c and b == e and b != a and a != d or b == d and b == e and b != a and a != c or c == d and c == e and c != a and a != b

#Función lógica que devuelve True, si la secuencia de argumentos es ascendente o iguales

def secuenciaAsc1(a, b) : 
    return a <= b 

def secuenciaAsc2(a, b, c) :
    return a <= b and b <= c 

def secuenciaAsc3(a, b, c, d) : 
    return a <= b and b <= c and c <= d 

def secuenciaAsc4(a, b, c, d, e) : 
    return a <= b and b <= c and c <= d and d <= e

#Función lógica que devuelve True, si la secuencia de argumentos es decreciente o iguales.

def secuenciaDesc1(a, b) : 
    return a >= b 

def secuenciaDesc2(a, b, c) : 
    return a >= b and b >= c 

def secuenciaDesc3(a, b, c, d) : 
    return a >= b and b >= c and c >= d 

def secuenciaDesc4(a, b, c, d, e) :
    return a >= b and b >= c and c >= d and d >= e

#Función lógica que devuelve True, si la secuencia de argumentos es la misma en ambos sentidos, es decir se secuencia de izquierda a derecha es la misma que la secuencia de derecha a izquierda.

def palindrome1(a, b) :
    return a == b 

def palindrome2(a, b, c) : 
    return a == c

def palindrome3(a, b, c, d) : 
    return a == d and b == c

def palindrome4(a, b, c, d, e) : 
    return a == e and b == d 

# Función Lógica que devuelve True, si los argumentos de la función forman poker. (Todos son iguales excepto uno)

def poker1(a, b) :
    return a != b

def poker2(a, b, c) : 
    return a == b and a != c or a == c and a != b or b == c and b != a ;

def poker3(a, b, c, d) : 
    return a == b and a == c and a != d or a == b and a == d and a != c or a == c and a == d and a != b or b == c and b == d and b != a  

def poker4(a, b, c, d, e) : 
    return a == b and a == c and a == d and a != e or a == b and a == c and a == e and a != d or a == b and a == d and a == e and a != c or a == c and a == d and a == e and a != b or b == c and b == d and b == e and b != a 

# Función lógica que devuelve True, un argumento es igual a la suma de todos los otros argumentos.

def sumados1(a, b, c) : 
    return a + b == c or a + c == b or b + c == a

def sumados2(a, b, c, d) : 
    return a + b + c == d or a + b + d  == c or a + c + d == b or b + c + d == a

def sumados3(a, b, c, d, e) : 
    return a + b + c + d == e or a + b + c + e == d or a + b + d + e == c or a + c + d + e == b or b + c + d + e == a


#Función lógica que devuelve True, si entre los argumentos existe un argumento que es igual a la división entera de otros dos argumentos.



#Función Lógica que devuelve True, todos los argumentos de la función son enteros positivos.

def positivos1(a) :
    return a > 0
print(positivos1(2))



def positivos2(a, b) : 
    return a > 0 and b > 0

def positivos3(a, b, c) : 
    return a > 0 and b > 0 and c > 0 

#Función Lógica que devuelve True, si todos los argumentos de la función son enteros negativos.

def negativos1(a) : 
    return a < 0 

def negativos2(a, b) : 
    return a < 0 and b < 0 

def negativos3(a, b, c) : 
    return a < 0 and b < 0 and c < 0 

# Función Lógica que devuelve True, si entre todos los argumentos existen argumentos positivos y argumentos negativos.

def positivoNeg1(a, b) :
    return a > 0 and b < 0 or a < 0 and b > 0 

def positivoNeg2(a, b, c) :
    return a > 0 and b > 0 and c < 0 or a > 0 and b < 0 and c > 0 or a < 0 and b > 0 and c > 0 or a < 0 and b < 0 and c > 0 or a < 0 and b > 0 and c < 0 or a > 0 and b < 0 and c < 0

#Función Lógica que devuelve True, si el entero n, es un entero positivo de un solo dígito. Si el entero n, tiene más de dos dígitos devuelve false.

def unDigitoPos(n) :
    return n > 0 and n < 10 

#Función Lógica que devuelve True, si el entero n, es un entero negativo de un solo dígito.

def unDigitoNeg(n) : 
    return n < 0 and n > -10 

#Función Lógica que devuelve True, si todos los argumentos son enteros positivos de dos dígitos.

def dosDigitosPos1(a) : 
    return a > 9 and a < 100 

def dosDigitosPos2(a, b) : 
    return a > 9 and a < 100 and b > 9 and b < 100

def dosDigitosPos3(a, b, c) :
    return a > 9 and a < 100 and b > 9 and b < 100 and c > 9 and c < 100

# Función Lógica que devuelve True, si todos los argumentos son enteros negativos de dos dígitos.

def dosDigitosNeg1(a) :
    return a < -9 and a > -100

def dosDigitosNeg2(a, b) : 
    return a < -9 and a > -100 and b < -9 and b > -100 

def dosDigitosNeg3(a, b, c) : 
    return a < -9 and a > -100 and b < -9 and b > -100 and c < -9 and c > -100

#Función Lógica que devuelve True, si todos los argumentos son enteros negativos de tres dígitos.

def tresDigitosNeg1(a) : 
    return a < -99 and a > -1000

def tresDigitosNeg2(a, b) :
    return a < -99 and a > -1000 and b < -97 and b > -1000

def tresDigitosNeg3(a, b, c) : 
    return a < -99 and a > -1000 and b < -99 and b > -1000 and c < -99 and c > -1000

#Función Lógica que devuelve True, si todos los argumentos de la función son enteros de un solo dígito y pueden ser positivos y/o negativos.

def unDigito1(a) : 
    return a > -10 and a < 10 

def unDigito2(a, b) : 
    return a > -10 and a < 10 and b > -10 and b < 10

def unDigito3(a, b, c) :
    return a > -10 and a < 10 and b > -10 and b < 10 and c > -10 and c < 10 

#Función Lógica que devuelve True, si todos los argumentos de la función son enteros de dos dígito y pueden ser positivos y/o negativos.
 
def dosDigitos1(a) : 
    return a > -100 and a < -9 or a > 9 and a < 100

def dosDigitos2(a, b) : 
    return a > -100 and a < -9 or a > 9 and a < 100 and b > -100 and b < -9 or b > 9 and b < 100

def dosDigitos3(a, b, c) : 
    return a > -100 and a < -9 or a > 9 and a < 100 and b > -100 and b < -9 or b > 9 and b < 100 and c > -100 and c < -9 or c > 9 and c < 100

#Función Lógica que devuelve True, si todos los argumentos de la función son enteros de tres dígitos y pueden ser positivos y/o negativos.

def tresDigitos1(a) : 
    return a > -1000 and a < -99 or a > 99 and a < 1000
 
def tresDigitos2(a, b): 
    return a > -1000 and a < -99 or a > 99 and a < 1000 and b > -1000 and b < -99 or b > 99 and b < 1000

def tresDigitos3(a, b, c) : 
    return a > -1000 and a < -99 or a > 99 and a < 1000 and b > -1000 and b < -99 or b > 99 and b < 1000 and c > -1000 and c < -99 or c > 99 and c < 1000

