
def suma_cifrelor(n:int)->int:
    s=0 
    while(n!=0):
        uc=n%10
        s=s+uc
        n=n//10
    return s
#### 1234 -> "1234"  = "4" => 4 

def suma_cifrelor_py(n:int)->int:
   return sum( int(c) for c in str(n))


def test_suma_cifre() -> None:
    print("n=")
    n = int(input())
    print("Suma cifrelor lui "+str(n))
    print(suma_cifrelor(n))
    print(suma_cifrelor_py(n))



  
def numar_cifre(n:int)->int:
    nr=0
    while(n!=0):
        nr+=1
        n=n//10
    return nr  
### 84579->"84579" =>5
def nr_cifrelor_py(n:int)->int:
    return len(str (n))

def test_numar_cifre() -> None:
    print("n=")
    n=int(input())
    print("Numarul cifrelor lui "+str(n))
    print(numar_cifre(n))
    print(nr_cifrelor_py(n))

def ogl_numar(n:int)->int:
    ogl=0
    while (n!=0):
        uc=n%10
        ogl=ogl*10+uc
        n=n//10
    return ogl


def palindrom(n:int)->bool:
    return n==ogl_numar(n)

def palindrom_py(n:int)->bool:
    return str(n)==str(n)[::-1]


def cifra_maxima_py(n:int)->tuple[int,int]:
    s=str(n)
    m=max(s)
    return [int(m),s.count(m)]

def test_palindrom()->None:
    print("n= ")
    n=int(input())
    if(palindrom(n)):
        print("DA")
    else:
        print("NU")

    if(palindrom_py(n)):
        print("DA")
    else:
        print("NU")
