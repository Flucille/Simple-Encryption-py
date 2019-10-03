#Fitzgerald 20/4/2018


import string


def encryption():
    
    key = 3
    key = int(key)
    i = 0
    message = input("Please enter a message that you would like to encrypt: ")
    print ('Encrypting Message')

    for i in range(3):
        print ('... Loading ...')
        i = (i+1)
    
    print ('')
    for letter in message:
            print (chr(ord(letter) + key))
            with open("EncryptedText.txt", "a") as File:
                File.write((chr(ord(letter) + key)))
                File.close

def decryption():
    s = "-";
    decryptedMessage = []
    Message = []
    i = (0)
    key = 3
    key = int(key)

    print ('Decrypting Message')

    for i in range(3):
        print ('... Loading ...')
        i = (i+1)

    print ('')
    
    i = (0)
    f = open("EncryptedText.txt","r") 
    for line in f:
        Message.append(line)
    print(Message)

    for i in  range(len(Message)):
        for letter in Message[i]:
            temp = (chr(ord(letter) - key))
            decryptedMessage.append(temp)
        i = (i+1)
    print (s.join(decryptedMessage))

    
    
print ('')
encryption()
print ('')
decryption()
    
