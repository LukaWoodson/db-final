from printUtils import colors as c, printColor

def getInputInt(message):
    userInput = getInput(message, c.UNDERLINE)
    try:
        return int(userInput)
    except ValueError:
        printColor('Must be a number', c.WARNING)
        return getInputInt(message)

def getInputBool(message):
    userInput = getInput(message, c.UNDERLINE)
    if userInput == 'y': return True
    elif userInput == 'n': return False
    else: 
        printColor('Invalid Input', c.WARNING)
        return getInputBool(message)

def getInputStr(message):
    userInput = getInput(message, c.UNDERLINE)
    if not userInput.strip():
        printColor('Not a valid string', c.WARNING)
        return getInputStr(message)
    else:
        return userInput

def getInput(message, color):
    return input(f'{color}{message}:{c.BASE} ')