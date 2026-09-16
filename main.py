import modules

print(modules.messageWelcome.center(50,"*"))
while(True):
    userChoice = input(modules.userChoiceMessage)
    if(userChoice.upper() not in ["ENCODE" , "DECODE"]):
        print("*".center(50,"*"))
        print("Please enter a valid choice!")
        print("*".center(50,"*"))
    else:
        if(userChoice.upper() == "ENCODE"):
            message1 = input(modules.messageToWillEncodeDecode)
            while(True):
                shift = input("Please enter your shift number to encode:")
                isValid = modules.validator(shift)
                if(isValid == True):
                    break
                else:
                    print("*".center(50,"*"))
                    print("Please enter a valid number!")
                    print("*".center(50,"*"))
                    continue
            modules.shiftNum = int(shift) % len(modules.alphabet)
            encodedMessage = modules.encode(message1)
            print("Your encoded message : {}".format(encodedMessage))
            break
        elif(userChoice.upper() == "DECODE"):
            message2 = input(modules.messageToWillEncodeDecode)
            while(True):
                shift = input("Please enter your shift number to decode:")
                isValid = modules.validator(shift)
                if(isValid == True):
                    break
                else:
                    print("*".center(50,"*"))
                    print("Please enter a valid number!")
                    print("*".center(50,"*"))
                    continue
            modules.shiftNum = int(shift) % len(modules.alphabet)
            decodedMessage = modules.decode(message2)
            print("Your decoded message : {}".format(decodedMessage))
            break
