from random import randint

#############################################################################################
# Modular Exponentiation Algorithm in python
#
# Used pseduo code from book, chapter 3 Excersise 23 part b
# Takes in three variables (x,a,n) and returns x^(a)mod n
##############################################################################################
def ModExponentiation(x,a,n):
   e = a
   b = 1
   c = x

   while e > 0:
       if e % 2 == 0:
           e = e//2
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
        a = randint(1,n-1)

        b = ModExponentiation(a,n-1,n)
        #test weather a^(n-1) mod n is not prime
        if b != 1:
            return False

        return True
###############################################################################################
# Recursive function for Extend Euclids algorithm
#
# I refrenced pseduo code from this website https://www.csee.umbc.edu/~chang/cs203.s09/exteuclid.shtml
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
        #continue preforming EEA
        d, x, y = EEA(b % a, a)
        return (d, y-(b//a)*x,x)

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
    d, x, y = EEA(b, n)
    if d == 1:
        return x % n

################################################################################################
# Generate Prime numbers function
#
# This function generates two 100 digit prime numbers for the public and private keys.
# By using randint from the random python library, we can generate 100 digit numbers.
# Then we check those numbers for primality by running them through the Fermats function.
# Repeat this process until two prime numbers are found.
#################################################################################################

def GeneratePrimes():

    a = randint(10**(100-1),(10**100)-1)

    #Check if 100 digit number is prime, if it is not repeat until prime number is found
    while not FermatsTest(a):
         a = randint(10**(100-1),(10**100)-1)
       
    b = randint(10**(100-1),(10**100)-1)
    while not FermatsTest(b):
         b = randint(10**(100-1),(10**100)-1)
      
    return (a,b)

####################################################################################################
# Generate Keys function
#
# Generate public and private keys. Using the e given to us from rubric, we find the public key
# is just ((p*q),e) and the private key is the multiplicative inverse of e and (p-1)*(q-1).
# Outputs both keys into sepreate files public_key and private_key
#####################################################################################################
def GenerateKeys():
    p,q = GeneratePrimes()
    # I am assuming from the assignment we can use the 65537 number as the e for the public key
    e = 65537

    public = (p*q,e)
    x = (p-1)*(q-1)

    private = mulinv(e,x)

    #writes the public and private key to there corresponding files
    pub = open("public_key","w+")
    pub.write('{}'.format(public))
    pub.close()

    priv = open("private_key","w+")
    priv.write('{}'.format(private))
    priv.close()

    #returns the public and private keys for display purposes if needed
    return (public,private)



