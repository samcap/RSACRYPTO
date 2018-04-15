import re
import KeySetup
import Encryption

def Decrypt():
    

def GetPrivateKey():

    file = open("private_key","r")
    if file.mode == 'r':
        PrivateKey = file.read()
    else:
        print("File failed to open")
        return(False)

    return(int(PrivateKey))

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

def Decode(s):
    c = 1
    count = 1
    message = ""
    
    
    for i in range (len(s)):
        first = True
        c = 1
        count = 1
        while c != 0:
            if first:
                c = s[i] % 256
                message += chr(c)
                first = False
                
            else:
                c = (s[i] - c)//(256**count) % 256
                if c == 0:
                    break
                message += chr(c)
                count += 1

    return(message)

cipher = Decrypt()
print(cipher)


