from random import randrange
#############################################################################################
# Modular Exponentiation Algorithm in python
#
# Takes in three variables (x,a,n) and returnsx^(a)mod n
# Algorithm taken from Excersise 23 part b from book
##############################################################################################
def ModExponentiation(x,a,n):
   e = a
   b = 1
   c = x

   while e > 0:
       if e % 2 == 0:
           e = e/2
           c = (c * c) % n
       else:
           e = e-1
           b = (b*c) % n

   return b
##############################################################################################
# Fermats Primality Test in python
#
# Takes in a suspected prime number n returns true if n is prime or false if n is not prime
# Runs the test 50 times with randomly generated a values
###############################################################################################
def FermatsTest(n):

    #check if n is 2
    if n == 2:
        return True
    #Check if even
    if n % 2 == 0:
        return False

    #run test 50 times
    for i in range (50):
        #compute random a for testing
        a = randrange(1,n-1)
        b = ModExponentiation(a,n-1,n)
        #test weather a^(n-1) mod n is not prime
        if b != 1:
            return False

        return True
###############################################################################################
# Recursive function for Extend Euclids algorithm
#
##############################################################################################
def EEA(a,b):
    if a == 0:
        return (b, 0 ,1)
    else:
        g, x, y = EEA(b % a, a)
        return (g, y-(b//a)*x,x)
def mulinv(b, n):
    g, x, _ = EEA(b, n)
    if g == 1:
        return x % n


def GeneratePrimes():
    a = randrange(1000000000,9999999999)
    while not FermatsTest(a):
         a = randrange(1000000000,9999999999)
       
    b = randrange(1000000000,9999999999)
    while not FermatsTest(b):
         b = randrange(1000000000,9999999999)
      
    return (a,b)

def GenerateKeys():
    p,q = GeneratePrimes()
    e = 65537

    public = (p*q,e)
    x = (p-1)*(q-1)
    private = mulinv(e,x)

    return (public,private)

keys = GenerateKeys()
print (keys)
