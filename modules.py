alphabet = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"]
messageWelcome = "Welcome To Ceaser Cipher"
messageToWillEncodeDecode = "Please enter your message:"
isValidShiftNum = False
shiftNum = 0
userChoiceMessage = "Do you want to decode or encode your message ? (Choices : Decode | Encode):"

def validator(shiftNumber):
    global isValidShiftNum
    try:
        shiftNumber = int(shiftNumber)
        isValidShiftNum = True
        return isValidShiftNum
    except(ValueError):
        return isValidShiftNum

def encode(message):
    global shiftNum
    encodedMessage = []
    for char in message:
        if(char.upper() not in alphabet):
            encodedMessage.append(char)
        elif(char.upper() in alphabet):
            oldİndex = alphabet.index(char.upper())
            newİndex = oldİndex + shiftNum
            if(newİndex >= len(alphabet)):
                newİndex = newİndex % len(alphabet)
            encodedMessage.append(alphabet[newİndex])
    return "".join(encodedMessage)        

def decode(message):
    global shiftNum
    decodedMessage = []
    for char in message:
        if(char.upper() not in alphabet):
            decodedMessage.append(char)
        elif(char.upper() in alphabet):
            oldİndex = alphabet.index(char.upper())
            newİndex = oldİndex - shiftNum % len(alphabet)
            decodedMessage.append(alphabet[newİndex])
    return "".join(decodedMessage)

