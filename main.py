def init():
    stack = []

    while True:
        doGUI()
        command = checkCommand()
        if command == 0:
            readAndPush(stack)
        elif command == 1:
            readAndPop(stack)
        elif command == 2:
            displayTop(stack)
        elif command == 3:
            exitApp()

    
    
def readAndPush(stack):




def readAndPop(stack):





def displayTop(stack):






def exitApp():



if __name__ == "__main__":
    init()