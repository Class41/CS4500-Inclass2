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

    
    
def readAndPush(stack):




def readAndPop(stack):





def displayTop(stack):






def exitApp():




def doGUI(nextPrint):
    guiOut = "/** Choose an action by number **\\\n\t0 -> Push to stack\n\t1 -> Pop to stack\n\t2 -> See top of stack\n\t3 -> Exit\n" + nextPrint
    print(guiOut)


if __name__ == "__main__":
    init()