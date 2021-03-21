#Nicholas Bryan - 201531951
#COMP517 - CA2 Looping Calculator

#define global variables x and y for calculations
x = 0
y = 0


## FUNCTIONS FOR CALCULATOR 1: SUMMATION

#function to find sum of two numbers (ints or floats) x and y
def sum(x,y):
    sumAns = x + y
    return sumAns

#function to take user input for calculation of sum and print result
def calcSummation():
    x = float(input("x = "))
    y = float(input("y = "))
    sumResult = sum(x, y)
    print("Sum of", x, "and", y, "is", sumResult)
    return


## FUNCTIONS FOR CALCULATOR 2: PRODUCT

#function to find product of two positive numbers x and y, where x is an int or float and y is int
def prod(x,y):
    prodAns = 0
    #adds x, y times
    for _ in range(0,y):
        prodAns = prodAns + x
    return prodAns

#function to take user input for calculation of product and print result
def calcProduct():
    x = float(input("x = "))
    y = int(input("y = "))
    #check if numbers are positive. If either x or y is negative, an error is displayed and function is restarted
    if x < 0 or y < 0:
        print("Invalid input: please enter positive numbers only")
        calcProduct()
    #finds the product of x and y, then prints result
    else:
        productResult = prod(x,y)
        print("Product of", x, "and", y, "is", productResult)
    return


## FUNCTIONS FOR CALCULATOR 3: EXPONENT

#function to find the value of x to the power of y, where x and y are two positive integers
def exp(x,y):
    #if exponent is zero, answer is 1
    if y == 0:
        expAns = 1
        return expAns
    else:
        #assigns x as the answer, then performs y-1 iterations of product function, such that when y = 1, the answer = x
        expAns = x
        for _ in range(1,y):
            #for y > 1, product function takes previous value of expAns (i.e. x to power of n-1) and multiplies it by x
            expAns = prod(expAns,x)
        return expAns

#function to take user input for calculation of exponent and print result
def calcExponent():
    x = int(input("x = "))
    y = int(input("y = "))
    #check if numbers are positive. If either x or y is negative, an error is displayed and function is restarted
    if x < 0 or y < 0:
        print("Invalid input: please enter positive numbers only")
        calcExponent()
    #check if x and y are both zero, answer is undefined, so function is restarted
    elif x == 0 and y == 0:
        print(x, "to the power of", y, "is undefined")
        calcExponent()
    else:
        #finds value of x to power of y and prints result
        exponentResult = exp(x,y)
        print(x, "to the power of", y, "is", exponentResult)
    return


## FUNCTIONS FOR CALCULATOR 4: MODULO

#function to find modulo of two positive numbers (ints or floats) x and y
def modulo(x,y):
    #assigns value of x to variable modAns
    modAns = x
    #checks if modAns is greater than or equal to y
    while modAns >= y:
        #if true, enters while loop and updates value of modAns to be modAns - y (using modAns and negative y in the sum function)
        #then checks if value is still greater than or equal to y
        modAns = sum(modAns,-y)
    return modAns

#function to take user input for calculation of modulo and print result
def calcModulo():
    x = float(input("x = "))
    y = float(input("y = "))
    #check if numbers are positive. If either x or y is negative, an error is displayed and function is restarted
    if x < 0 or y < 0:
        print("Invalid input: please enter positive numbers only")
        calcModulo()
    #check if y is zero, answer is undefined, so function is restarted
    elif y == 0:
        print(x, "modulo", y, "is undefined")
        calcModulo()
    else:
        #finds the value of x modulo y and prints result
        moduloResult = modulo(x,y)
        print(x, "modulo", y, "is", moduloResult)
    return


## FUNCTION & LOOP FOR MAIN MENU

#function for evaluation of user's main menu selection, calls relevant function if true, else returns to main menu
def evalMainMenu(mainMenuInput):
    if mainMenuInput == "1":
        print("[1] Summation\nEnter two numbers x and y")
        calcSummation()
    elif mainMenuInput == "2":
        print("[2] Product\nEnter two positive numbers x and y, where x is an integer or float and y is integer")
        calcProduct()
    elif mainMenuInput == "3":
        print("[3] Exponent\nEnter two positive integers x and y, where x is raised to the power of y")
        calcExponent()
    elif mainMenuInput == "4":
        print("[4] Modulo\nEnter two positive numbers x and y")
        calcModulo()
    elif mainMenuInput == "q":
        exit()
    else:
        print("Invalid input: please enter [1], [2], [3], [4] or [q] to select option")
        return

mainMenuInput = 0
#while loop prints main menu options and requests input, which is entered as the parameter in function evalMainMenu 
while(mainMenuInput == 0):
    print("\nLooping Calculator\nMAIN MENU")
    print("[1] Summation")
    print("[2] Product")
    print("[3] Exponent")
    print("[4] Modulo")
    print("[q] Exit")
    evalMainMenu(input("\nSelect option and press [Enter] key:"))