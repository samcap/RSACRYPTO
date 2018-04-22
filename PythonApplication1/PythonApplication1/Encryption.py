import re
import math
import KeySetup

#############################################################################################
# GetPubKey function 
#
# This function is used to read in the public key from the public_key file
# Then returns the public key
#############################################################################################
def GetPubKey():

    file = open("public_key","r")

    if file.mode == 'r':
        fileKey = file.read()
    else:
        print("File failed to open")
        return(False)

    #parses the public key from the file. The first sub string is 
    #k and the second substring is e.

    keystring = fileKey.split(',')
    k = re.sub("[^0-9]", "", keystring[0])
    e = re.sub("[^0-9]", "", keystring[1])
    pubKey = (int(k),int(e))

    file.close()
    return(pubKey)

#############################################################################################
# GetPlainText function 
#
# This function is used to read in the plain text from the PlainText.txt file
# Then returns the plaintext
#############################################################################################
def GetPlainText():
    file = open("PlainText.txt","r")
    if file.mode == 'r':
        plaintext = file.read()
    else:
        print("File failed to open")
        return(False)
    file.close()

    return plaintext

#############################################################################################
# Encode function 
#
# This fucntion is used to encode the plaintext.
# The function will take in a plaintext and apply the encoding method outlined in the 
# Assignement document.
# By using ASCII we can change each char of PT into a number(0-256) and interprut every char as a byte.
# Then we sum each char together in a sumation formula k = m*256^(n) where n is the n-1 postion of the char
# in the plain text. 
# We do this for the first 81 chars save the sumation and then start over agian until all chars are read
# we stop at the first 81 chars because the encoded number needs to be smaller than n in the private key
#############################################################################################

def Encode(pt):
    length = len(pt)
    s = []
    exp = 1
    m = 0
    start = False

    #read in the chars from the plain text
    for i in range(length):
        # check if we are at the 81st char or the very beggging of the Plain Text
        # If it is the first char we just add the ascii number to m
        if i % 81 != 0 or i == 0:
            if not start:
                m += ord(pt[i])
                start = True
            # when not the 81st char or the first char of th message we apply the 
            # exponent and add to m
            else:
                m += ord(pt[i])*256**exp
                exp+=1
        else:
            # When we reach the 81st char we add the value to m
            # and reset the variables to start encoding the next 81 chars.
            # we append the previous 81 chars to an integer array

            m += ord(pt[i])*256**exp
            s.append(m)
            m = 0
            exp = 1
            start = False

    s.append(m)
    print(s)
    return s

#############################################################################################
# Encrypt function 
#
# This function gets all the information needed to apply the RSA encryption algorithm from the
# assignemnt doc and output the result to the ciphertext file.
# This function will take the encoded plain text parts and encrypt to make the cipher text by 
# c = k^e (mod n).
# where c is the cipher text, k are the parts of the encoded text, e and n are from the public
# key.
#############################################################################################
def Encrypt():
    # get the public key, plaintext, and encode the plain text
    pubkey = GetPubKey()
    plaintext = GetPlainText()
    k = Encode(plaintext)
    ciphertext = []

    #for all the encoded plaintext segments apply the algorithm
    for i in range(len(k)):
        c = KeySetup.ModExponentiation(k[i],pubkey[1],pubkey[0])
        ciphertext.append(c)

    # Wrtie the resulting cipher text to the ciphertext file.
    file = open("ciphertext","+w")
    
    file.write('{}'.format(ciphertext))
    file.close()






