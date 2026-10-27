
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