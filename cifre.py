# suma cifrelor  unui numar
from math import isqrt


def suma_cifrelor(n:int)->int:
    return sum(int(c) for c in str(n))

def suma_cifrelor2(n:int)->int:
    suma=0
    for cifra in str(abs(n)) :
        suma+=int(cifra)
    return suma

def test_suma_cifrelor()->None:
        print("n=")
        n=int(input())
        print(suma_cifrelor(n))

def numar_palindrom(n:int)->bool:
     return str(n)==str(n)[::-1]

def test_palindrom()->None:
    n=8338
    print(numar_palindrom(n))

def cifra_maxima(n:int)->tuple[int,int]:
     s=str(n)
     m=max(s)
     return  int(m), s.count(m)

def test_cifra_maxima()->None:
     n=19697
     maxim ,aparitii= cifra_maxima(n)
     print(maxim)
     print(aparitii)


def este_prim(n:int)->bool:
     if(n<2):
          return False
     divizori_posibili=range(2,isqrt(n)+1)  ###[ 2,3,4,5]
     nu_se_divide=[n%d!=0 for d in divizori_posibili] ##### [true,true,true,true]

     return all(nu_se_divide)

def test_prim()->None:
     n=12
     print(este_prim(n))


########   un numar este  perfect daca este egal cu suma divizorilor lui , fara el insusi
def numar_perfect(n:int)->int:
       divizori=[d for d in range(1,n) if n%d==0]
       suma_divizorilor=sum(divizori)
       return suma_divizorilor == n

def test_perfect()->None:
     n=496
     print(numar_perfect(n))

def cifra_de_control(n:int)->int:
     while sum>10:
        sum=suma_cifrelor(n)

def test_control(n:int)->None:
     n=13455
     print(cifra_de_control(n))


#####  c   cifra  cifra%2==1  rezultat
##### "1"    1       da         "11"
##### "2"    2       nu         "112"  
##### "4"    4       nu         "1124"
##### "5"    5       da         "112455"
##### "6"    6       nu         "1124556"
def dubleaza_impare(n:int)->int:
     rezultat=""
     for c in str(n):
          cifra=int(c)
          if cifra%2==1:
               rezultat+=c*2
          else:
               rezultat+=c
     return rezultat

def test_dublare()->None:
     n=12456
     print(dubleaza_impare(n))


