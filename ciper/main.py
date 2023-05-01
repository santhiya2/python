import decryptMessage
import getCipherKey
import getmessage
import getDoubleAlphabet
import encryptMessage

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet.getDoubleAlaphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getmessage.getmessage()
    print(myMessage)
    myCipherKey = getCipherKey.getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage.encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage.decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()