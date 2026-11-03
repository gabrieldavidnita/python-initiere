
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

def cifre_pare(n:int)->int:
    nr=0
    p=1

    if n==0:
        return 0

    while(n!=0):
        uc=n%10
        if uc%2==0:
            nr=uc*p+nr
            p=p*10
        n=n//10

    if p==1:
        return -1
    return nr

def cifre_pare_py(n:int)->int:
    nr=0
    gasit=False

    for c in str(n):
        uc=int(c)
        if uc%2==0:
            nr=nr*10+uc
            gasit=True

    if gasit:
        return nr
    return -1

def test_cifre_pare()->None:
    print("n=")
    n=int(input())
    print(cifre_pare(n))
    print(cifre_pare_py(n))


def sterge_cifra(n:int,c:int)->int:
    nr=0
    p=1
    if n==0:
        if c==0:
            return -1
        return 0
    while(n!=0):
        uc=n%10
        if uc!=c:
            nr=uc*p+nr
            p=p*10
        n=n//10
    if p==1:
        return -1
    return nr

def sterge_cifra_py(n:int,c:int)->int:
    nr=0
    gasit=False

    for cifra in str(n):
        uc=int(cifra)
        if uc!=c:
            nr=nr*10+uc
            gasit=True

    if gasit:
        return nr
    return -1

def test_sterge_cifra()->None:
    print("n=")
    n=int(input())
    print("c=")
    c=int(input())
    print(sterge_cifra(n,c))
    print(sterge_cifra_py(n,c))


    def ogl_numar(n:int)->int:
     ogl=0

    while(n!=0):
        uc=n%10
        ogl=ogl*10+uc
        n=n//10

    return ogl

def este_prim(n:int)->bool:
    if n<2:
        return False

    d=2
    while(d*d<=n):
        if n%d==0:
            return False
        d=d+1

    return True

def este_prim_py(n:int)->bool:
    return este_prim(n)

def prim_si_oglindit(n:int)->bool:
    return este_prim(n) and este_prim(ogl_numar(n))

def prim_si_oglindit_py(n:int)->bool:
    ogl=int(str(n)[::-1])
    return este_prim_py(n) and este_prim_py(ogl)

def test_prim_si_oglindit()->None:
    print("n=")
    n=int(input())
    print(prim_si_oglindit(n))
    print(prim_si_oglindit_py(n))