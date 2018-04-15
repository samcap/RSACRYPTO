from random import randrange
#############################################################################################
# Modular Exponentiation Algorithm in python
#
# Takes in three variables (x,a,n) and returns x^(a)mod n
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
# Runs the test 50 times with randomly generated (a) values
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
# Takes in two numbers to find the GCD. Then will find the 2 variables to find the linear combination
# that proves the GCD. The program will return a tuple where the frist number is the gcd and
# the other two numbers are the the variables found in the extend part of EEA
##############################################################################################

def EEA(a,b):

    #Found gcd
    if a == 0:
        return (b, 0 ,1)

    else:
        # To continue the algorithm we recursivly call EEA with the mod of b and a, and a
        # Then if we have not finished the algorithm we format the return as g being the last
        # remander from the previous run, x is y-(b floor a) * x, and y is shifted to be x 
        g, x, y = EEA(b % a, a)
        return (g, y-(b//a)*x,x)

################################################################################################
# Multiplicative Inverse function
#
# Finds the multiplicative inverse by taking in two numbers
# Apply euclids extended algorithm, if the gcd of b and n is 1 than the multiplicative inverse is
# the remainder of the first variable in the linear combination and n.
#################################################################################################
def mulinv(b, n):

    # All we neeed is the gcd and first variable of the linear combination,
    # we can ignore the last part of the tuple
    g, x, _ = EEA(b, n)
    if g == 1:
        return x % n

################################################################################################
# Generate Prime numbers function
#
# This function generates two 10 digit prime numbers for the public and private keys.
# By using randrange from the random python library, we can generate 10 digit numbers.
# Then we check those numbers for primality by running them through the Fermats function.
# Repeat this process until two prime numbers are found.
#################################################################################################

def GeneratePrimes():

    a = randrange(1000000000,9999999999)

    #Check if 10 digit number is prime, if it is not repeat until prime number is found
    while not FermatsTest(a):
         a = randrange(1000000000,9999999999)
       
    b = randrange(1000000000,9999999999)
    while not FermatsTest(b):
         b = randrange(1000000000,9999999999)
      
    return (a,b)

####################################################################################################
# Generate Keys function
#
# Generate public and private keys. Using the e given to us from rubric, we find the public key
# is just ((p*q),e) and the private key is the multiplicative inverse of e and (p-1)*(q-1).
# Outputs both keys into sepreate files public_key.txt and private_key.txt
#####################################################################################################
def GenerateKeys():
    p,q = GeneratePrimes()
    e = 65537

    public = (p*q,e)
    x = (p-1)*(q-1)
    private = mulinv(e,x)

    pub = open("public_key","w+")
    pub.write('{}'.format(public))
    pub.close()

    priv = open("private_key","w+")
    priv.write('{}'.format(private))
    priv.close()


    return (public,private)


