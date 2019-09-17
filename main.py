def init():
    stack = []
    
    while True:
        doGUI()
        command = checkCommand()
        if command == 0:
            readAndPush()
        elif command == 1:
            readAndPop()
        elif command == 2:
            displayTop()
        elif command == 3:
            exitApp()

    
    
def readAndPush():





def readAndPop():





def displayTop()):






def exitApp():



if __name__ == "__main__":
    init()