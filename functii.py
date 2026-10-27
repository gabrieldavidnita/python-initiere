
def ultima_cifra(n:int)->int:
    ultima=n%10
    return ultima

def numar_cifre(n:int)->int:
    nr=0
    while(n!=0):
    n=n/10
    nr++
    return nr
