
def sumandos4(a, b, c, d) : 
    return (a + b + c) == d or (a + b + d) == c or (a + c + d) == b or (b + c + d) == a
print(sumandos4(2,3,4,5))

def dosDigitos1(a) : 
    return a > - 100 and a < - 9 or a > 9 and a < 100
print(dosDigitos1(3))

def tresDigitos1(a) :
    return a > - 1000 and a < - 99 or a > 99 and a < 1000
print(tresDigitos1(2))

def decreciente(a, b, c, d, e) : 
    return a >= b and b >= c and c >= d and d >= e
print(decreciente(2,3,4,5,6))

def tresIguales4(a, b, c, d) : 
    return a == b and a == c and a != d or a == b and a == d and a != c or a == c and a == d and a != b or b == c and b == d and b != a
print(tresIguales4(2,3,4,5))

def dosIguales3(a, b, c) :
    return a == b and a != c or a == c and a != b or b == c and b != a  
print(dosIguales3(2,3,4))