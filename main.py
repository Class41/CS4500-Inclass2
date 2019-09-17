def init():
    stack = []
    nextPrint = ""
    while True:
        doGUI(nextPrint)
        nextPrint = ""
        command = checkCommand()
        if command == 0:
            nextPrint = readAndPush(stack)
        elif command == 1:
            nextPrint = readAndPop(stack)
        elif command == 2:
            nextPrint = displayTop(stack)
        elif command == 3:
            exitApp()

    
    
#Debugging
stack.append("C")
stack.append("A")

#appending whatever character
def readAndPush(stack, c):
    stack.append(c)
    return stack

#popping off the last of the list
def readAndPop(stack):
    stack.pop()
    return stack

#Display last of the list
def displayTop(stack):
    return stack[-1]





def exitApp():
    sys.exit()



def doGUI(nextPrint):
    guiOut = "/** Choose an action by number **\\\n\t0 -> Push to stack\n\t1 -> Pop to stack\n\t2 -> See top of stack\n\t3 -> Exit\n" + nextPrint
    print(guiOut)


#Testing functions
readAndPush(stack, "T")
print(stack)

stack = readAndPop(stack)
print(stack)

print(displayTop(stack))



if __name__ == "__main__":
    init()