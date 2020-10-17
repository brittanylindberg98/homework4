def isPrime( x ):
    evenDivisions = 0
    if x <= 1:
        return False
    for currentNumber in range( 1, x + 1):
        if x % x ==0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True
import random
x = random.randint(1,100)
def main():
    if isPrime ( x ):
        print( x, "is a prime number" )
    else:
        print( x, "is not a prime number" )
main()
