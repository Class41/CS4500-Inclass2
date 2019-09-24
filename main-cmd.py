"""
# Authors: Vasyl Onufriyev, Caleb Freeman, Freddie Tao
# Date: 9.24.19
# Class: CS4500 Professor Keith Miller

# Purpose #
The purpose of this program is to assist the target audience in understanding how stacks work.
The program offers very simple stack operations such as pushing, popping, and peeking at the top
of the stack. As a side feature, it allows the user to see the stack.

# Runtime Info #
The program consists of a infinite loop which runs a menu, asks a user for a command, then executes the command. 
If any user input is required, the user is queried for the requested information. Stack is limited to a size of 10.
On successful operation, the stack is displayed along with a message. On failure, a error message is displayed and the user
is sent back to the menu phase.

# To run #
python3.7 main.py
"""
import turtle

stack = [] #Global stack, used for all functions. Prevents having to pass/return every time
maxStack = 10 #Sets max stack size

def init():
    global stack #Reference to global stack
    nextPrint = "" #What to print on the next iteration of the graphics display
    result = [True, "OK"] #True to display array, False to not, Message to display
    doGUI(nextPrint) #Print GUI

    while True:
        command = checkCommand() #Get user command
        nextPrint = ""
        result = [True, "OK"]
        
        if command != False: #Figure what the user wanted to do
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

# Check what command the user wants to do
def checkCommand(): 

    userSelection = input()
    try: #Try to parse an int from the input
        userSelection = int(userSelection)
        return userSelection
    except Exception as e:
        print("Unable to convert input to acceptable menu command.")
        return False

# Appending whatever character
def readAndPush():
    global stack
    
    if len(stack) >= maxStack: # Check stack bounds
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

# Exit program
def exitApp():
    exit()

# Display GUI
def doGUI(nextPrint):
    guiOut = "/** Choose an action by number **\\\n\t1 -> Push to stack\n\t2 -> Pop from stack\n\t3 -> See top of stack\n\t4 -> See Stack\n\t5 -> Exit\n\n" + nextPrint
    
    print(guiOut)

if __name__ == "__main__":
    init()
