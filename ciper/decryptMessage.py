import encryptMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage.encryptMessage(message, decryptKey, alphabet)