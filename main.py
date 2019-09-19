stack = []


def init():
    nextPrint = ""
    while True:
        doGUI(nextPrint)
        nextPrint = ""
        command = checkCommand()

        if command == 0:
            nextPrint = readAndPush()
        elif command == 1:
            nextPrint = readAndPop()
        elif command == 2:
            nextPrint = displayTop()
        elif command == 3:
            exitApp()

# appending whatever character


def readAndPush():
    global stack
    stack.append(c)
    return stack

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
