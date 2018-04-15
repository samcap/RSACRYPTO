import re
import math
import KeySetup

def GetPubKey():

    file = open("public_key","r")

    if file.mode == 'r':
        fileKey = file.read()
    else:
        print("File failed to open")
        return(False)
    
    keystring = fileKey.split(',')
    k = re.sub("[^0-9]", "", keystring[0])
    e = re.sub("[^0-9]", "", keystring[1])
    pubKey = (int(k),int(e))

    file.close()
    return(pubKey)

def GetPlainText():
    file = open("PlainText.txt","r")
    if file.mode == 'r':
        plaintext = file.read()
    else:
        print("File failed to open")
        return(False)
    file.close()

    return plaintext


def Encode(pt):
    length = len(pt)
    s = []
    exp = 1
    m = 0
    start = False
    for i in range(length):
        if i % 82 != 0 or i == 0:
            if not start:
                m += ord(pt[i])
                start = True
            else:
                m += ord(pt[i])*256**exp
                exp+=1
        else:
            m += ord(pt[i])*256**exp
            s.append(m)
            m = 0
            exp = 1
            start = False
    s.append(m)
    return s

def Encrypt():

    pubkey = GetPubKey()
    plaintext = GetPlainText()
    k = Encode(plaintext)
    ciphertext = []

    for i in range(len(k)):
        c = KeySetup.ModExponentiation(k[i],pubkey[0],pubkey[1])
        ciphertext.append(c)

    file = open("ciphertext","+w")
    file.write('{}'.format(ciphertext))
    file.close()


             
def main():

   Encrypt()

   
main()


