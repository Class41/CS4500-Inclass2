stack = []

def init():
    nextPrint = ""
    result = [True, "OK"]
    
    while True:
        doGUI(nextPrint)
        command = checkCommand()
        if command == 0:
            result = readAndPush()
        elif command == 1:
            result = readAndPop()
        elif command == 2:
            result = displayTop()
        elif command == 3:
            exitApp()
        
        

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
    stack.pop()
    return stack

# Display last of the list
def displayTop():
    global stack
    return stack[-1]


def exitApp():
    exit()


def doGUI(nextPrint):
    guiOut = "/** Choose an action by number **\\\n\t0 -> Push to stack\n\t1 -> Pop to stack\n\t2 -> See top of stack\n\t3 -> Exit\n" + nextPrint
    print(guiOut)


if __name__ == "__main__":
    init()
