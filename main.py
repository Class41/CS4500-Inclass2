#Vasyl Onufriyev, Caleb Freeman, Freddie Tao

stack = []
maxStack = 10

def init():
    global stack
    nextPrint = ""
    result = [True, "OK"]
    doGUI(nextPrint)

    while True:
        command = checkCommand()
        nextPrint = ""
        result = [True, "OK"]
        
        if command != False:
            if command == 1:
                result = readAndPush()
            elif command == 2:
                result = readAndPop()
            elif command == 3:
                result = displayTop()
            elif command == 5:
                exitApp()
            
            nextPrint = result[1]
            
            if result[0] == True:
                print(str(stack))
            
        doGUI(nextPrint)
        
	pen = turtle.Turtle()
	pen.pensize(3)

	for box in range(10):
		DrawStack(pen)
	
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
    
    if len(stack) >= maxStack:
        return [False, "Stack is full! Max is 10!"]
        
    c = input("What character would you like to add to the stack?\n")
    
    if len(c) == 1:
        stack.append(c)
        return [True, "Added character to the stack."]
    else:
        return [False, "Too many characters entered! Was expecting 1!"]

# popping off the last of the list
def readAndPop():
    global stack
    
    if not stack:
        return[False, "Cannot pop an empty stack"]
	
    while True:
        c = input("You are about to remove " + str(stack[-1]) + " from the stack. \nIs this correct? Y for yes or N for No\n")
        if c.lower() == "y":
            popped = stack.pop()
            return [True, "Removed " + popped + " from the stack."]
        elif c == "n":
            print("Returning to main menu")
            return
        else:
            print("Invalid characters, please try again")
	

# Display last of the list
def displayTop():
    global stack
    if not stack:
        return[False, "Cannot see the top of an empty stack."]
    else:
        x = stack.pop()
        stack.append(x)
        return[True, x]

def exitApp():
    exit()


def doGUI(nextPrint):
    guiOut = "/** Choose an action by number **\\\n\t1 -> Push to stack\n\t2 -> Pop from stack\n\t3 -> See top of stack\n\t4 -> See Stack\n\t5 -> Exit\n\n" + nextPrint
    print(guiOut)

def DrawStack(pen):
    height = 25
    length = 100

    pen.forward(length)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(length)
    pen.right(90)
    pen.forward(height)
    pen.right(180)
    pen.forward(height)
    pen.left(90)



if __name__ == "__main__":
    init()
