import re
import KeySetup
import Encryption
#############################################################################################
# Decryption function
#
# This function applies the RSA decryption algorithm. k = c^d (mod n)
# where k is the encoded plain text, c is the cipher text, d is the private key and n is from the
# Public key
##############################################################################################
def Decrypt():
    # Get the private key, the public key and the cipher text
    d = GetPrivateKey()
    n = Encryption.GetPubKey()
    c = GetCipher()

    #apply the algorithm to get the encoded plain text
    DecryptedCipher = []
    for i in range(len(c)):
        DecryptedCipher.append(KeySetup.ModExponentiation(c[i],d,n[0]))
    return DecryptedCipher



#############################################################################################
# Get Private Key fucntion
#
# This function gets the private key from the file
##############################################################################################
def GetPrivateKey():

    file = open("private_key","r")
    if file.mode == 'r':
        PrivateKey = file.read()
    else:
        print("File failed to open")
        return(False)

    return(int(PrivateKey))


#############################################################################################
# GetCipher function
#
# This function gets the Cipher text key from the file. Needs to parse out the ,s from the file
##############################################################################################
def GetCipher():

    file = open("ciphertext","r")

    if file.mode == 'r':
        filecipher = file.read()
    else:
        print("File failed to open")
        return(False)

    textstring = filecipher.split(',')
    cipher = []
    for i in range(len(textstring)):
        cipher.append(int(re.sub("[^0-9]", "", textstring[i])))

    file.close()


    return(cipher)


#############################################################################################
# Decode function
#
# This function decodes the encode cipher text.
# The decoding works by takeing the cipher text (s) and dividing by 256^n-1 mod (256). If you have 
# already started the process then you also subtract the previous result from the encoded text.
##############################################################################################
def Decode(s):
    c = 1
    count = 1
    message = ""
    
    #Run the algorithm until all encoded text is decoded
    for i in range (len(s)):
        first = True
        c = 1
        count = 1
        while c != 0:
            #if first number just preform mod 256
            if first:
                c = s[i] % 256
                message += chr(c)
                first = False

            #if not the first number apply the rest of the algorithm
            else:
                c = (s[i] - c)//(256**count) % 256
                if c == 0:
                    break
                message += chr(c)
                count += 1
    #return the decrpyted message
    return(message)


KeySetup.GenerateKeys()
Encryption.Encrypt()
cipher = Decrypt()
print(Decode(cipher))


