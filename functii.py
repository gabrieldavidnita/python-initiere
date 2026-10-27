
def ultima_cifra(n:int)->int:
    ultima=n%10
    return ultima

def numar_cifre(n:int)->int:
    nr=0
    while(n!=0):
        nr+=1
        n=n//10
    return nr

def suma_cifre(n:int)->int:
    s=0 
    while(n!=0):
        uc=n%10
        s=s+uc
        n=n//10
    return s


def solutie1():
    print("Numarul are "+str(numar_cifre(21312))+"  cifre")

def solutie2():
    print("Numarul are suma cifrelor "+str(suma_cifre(2331)))