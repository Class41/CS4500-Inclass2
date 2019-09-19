#Vasyl Onufriyev, Caleb Freeman, Freddie Tao

stack = []

def init():
    global stack
    nextPrint = ""
    result = [True, "OK"]
    
    while True:
        doGUI(nextPrint)
        command = checkCommand()
        nextPrint = ""
        
        if command != False:
            if command == 0:
                result = readAndPush()
            elif command == 1:
                result = readAndPop()
            elif command == 2:
                result = displayTop()
            elif command == 3:
                exitApp()
            
            nextPrint = result[1]
            
            if result[0]:
                print(str(stack))
        
def checkCommand():
    userSelection = input()
    
    try:
        userSelection = int(userSelection)
        return userSelection
    except Exception as e:
        print("Unable to convert input to acceptable menu command.")
        return False

# appending whatever character
def readAndPush():
    global stack
    
    c = input("What character would you like to add to the stack?")
    if len(c) == 1:
        stack.append(c)
        return [True, "Added character to the stack."]
    else:
        return [False, "Too many characters added! Was expecting 1!"]

# popping off the last of the list
def readAndPop():
    global stack
    if not stack:
        return[False, "empty list"]
    else:
        x = stack.pop()
        return[True, x]

# Display last of the list
def displayTop():
    global stack
    if not stack:
        return[False, "empty list"]
    else:
        x = stack.pop()
        stack.append(x)
        return[True, x]

def exitApp():
    exit()


def doGUI(nextPrint):
    guiOut = "/** Choose an action by number **\\\n\t0 -> Push to stack\n\t1 -> Pop to stack\n\t2 -> See top of stack\n\t3 -> Exit\n\n\n" + nextPrint
    print(guiOut)


if __name__ == "__main__":
    init()
