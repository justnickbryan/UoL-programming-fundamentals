#Nicholas Bryan - 201531951
#COMP517 - CA1 Shapes

#missing internal angle calculator function: requests user to enter 2 known angles and performs calculation to give value of missing angle
def calcMissingAngle():
    print("\nMissing angle calculator\nCalculates a missing internal angle of any triangle to 2 decimal places, given 2 internal angles (in degrees)")
    #requests user to enter angle 1. Entry (made as a string) is typecast to float and rounded to 3 decimal places (dp) for reasonable accuracy in final calculation to 2 dp
    angle1InDegrees = round(float(input("Enter angle 1 (degrees): ")), 3)
    #if statement evaluates as TRUE if the entry is NOT a value between 0 and 180, then prints error message and restarts the function
    if(not 0 < angle1InDegrees < 180):
        print("Invalid entry, enter angle in degrees between 0 and 180")
        calcMissingAngle()
    #if statement evaluates as FALSE if the entry is a value between 0 and 180
    else:
        #angle 2 is entered, rounded and evaluated as above for angle 1
        angle2InDegrees = round(float(input("Enter angle 2 (degrees): ")), 3)
        if(not 0 < angle2InDegrees < 180):
            print("Invalid entry, enter angle in degrees between 0 and 180")
            calcMissingAngle()
        else:
            #sum of angles 1 and 2 is found
            sumAnglesInDegrees = angle1InDegrees + angle2InDegrees
            #if sum of angles is greater than or equal to 180 degrees, prints error message and returns to main menu
            if(sumAnglesInDegrees >= 180):
                print("Angle 1 + Angle 2 =", sumAnglesInDegrees, ">= 180 degrees.\nThere may be an error in your entry, or the shape is not a triangle!")
                return
            #if sum of angles is less than 180, calculates missing angle and rounds the value to 2 dp
            else:
                missingAngleInDegrees = round(180 - sumAnglesInDegrees, 2)
                print("\nAngle 1 =", angle1InDegrees, "degrees", "\nAngle 2 =", angle2InDegrees, "degrees", "\nMissing angle =", missingAngleInDegrees, "degrees")
                return

#length of hypotenuse calculator function: requests user to enter 2 known side lengths and performs calculation to give length of hypotenuse
def calcHypotenuse():
    print("\nHypotenuse calculator\nCalculates the length of the hypotenuse for any right-angled triangle to 2 decimal places, given the other 2 sides (in cm)")
    #requests side length 1 to be entered. Value is cast to float and rounded to 3 dp
    side1LengthInCm = round(float(input("Enter length of side 1 (in cm): ")), 3)
    #if statement evaluates as TRUE if the entry is NOT a value greater than 0, then prints error message and restarts the function
    if(not side1LengthInCm > 0):
        print("Invalid entry, side length must be greater than 0")
        calcHypotenuse()
    #if statement evaluates as FALSE if the entry is a value greater than 0
    else:
        #length of side 2 is entered, rounded and evaluated as above for side 1
        side2LengthInCm = round(float(input("Enter length of side 2 (in cm): ")), 3)
        if(not side2LengthInCm > 0):
            print("Invalid entry, side length must be greater than 0")
            calcHypotenuse()
        else:
            #calculates length of hypotenuse in cm and rounds the value to 2 dp
            hypotenuseInCm = round(((side1LengthInCm**2 + side2LengthInCm**2)**0.5), 2)
            print("\nSide 1 =", side1LengthInCm, "cm", "\nSide 2 =", side2LengthInCm, "cm", "\nHypotenuse =", hypotenuseInCm, "cm")
            return

#area of triangle calculator function: requests user to enter 3 known side lengths and performs calculation to give area of triangle
def calcArea():
    print("\nArea calculator\nCalculates the area of any triangle to 2 decimal places, given the lengths of all sides (in cm)")
    #requests side length 1 to be entered. Value is cast to float and rounded to 3 dp.
    side1LengthInCm = round(float(input("Enter length of side 1 (in cm): ")), 3)
    #if statement evaluates as TRUE if the entry is NOT a value greater than 0, then prints error message and restarts the function
    if(not side1LengthInCm > 0):
        print("Invalid entry, side length must be greater than 0")
        calcArea()
    #if statement evaluates as FALSE if the entry is a value greater than 0
    else:
        #length of side 2 is entered, rounded and evaluated as above for side 1
        side2LengthInCm = round(float(input("Enter length of side 2 (in cm): ")), 3)
        if(not side2LengthInCm > 0):
            print("Invalid entry, side length must be greater than 0")
            calcArea()
        else:
            #length of side 3 is entered, rounded and evaluated as above for sides 1 and 2
            side3LengthInCm = round(float(input("Enter length of side 3 (in cm): ")), 3)
            if(not side3LengthInCm > 0):
                print("Invalid entry, side length must be greater than 0")
                calcArea()
            else:
                #sum of pairs of sides is calculated
                sum1And2InCm = side1LengthInCm + side2LengthInCm
                sum1And3InCm = side1LengthInCm + side3LengthInCm
                sum2And3InCm = side2LengthInCm + side3LengthInCm
                #evaluates if the length of any side is greater than or equal to the sum of the other 2 sides, if true prints error message and returns to main menu
                if(side1LengthInCm >= sum2And3InCm or side2LengthInCm >= sum1And3InCm or side3LengthInCm >= sum1And2InCm):
                    print("There may be an error in your entry, or the shape is not a triangle!\nAny one side cannot have a length greater than or equal to the sum of the other two sides")
                    return
                else:
                    #calculates half-perimeter of triangle for use in area calculation (Heron's formula)
                    halfPerimeterInCm = (side1LengthInCm + side2LengthInCm + side3LengthInCm) / 2
                    #calculates area of triangle in cm squared and rounds the value to 2 dp
                    areaTriangleInCmSqrd = round((halfPerimeterInCm * (halfPerimeterInCm - side1LengthInCm) * (halfPerimeterInCm - side2LengthInCm) * (halfPerimeterInCm - side3LengthInCm))**0.5, 2)
                    print("\nSide 1 =", side1LengthInCm, "cm", "\nSide 2 =", side2LengthInCm, "cm", "\nSide 3 =", side3LengthInCm, "cm", "\nArea of Triangle =", areaTriangleInCmSqrd, "cm squared")
                    return

#function for evaluation of user's main menu selection
def evalMainMenu(x):
    #string is evaluated, if true missing angle calculator function is called
    if x == "1":
        calcMissingAngle()
    #evaluated, if true hypotenuse calculator called
    elif x == "2":
        calcHypotenuse()
    #evaluated, if true area calculator
    elif x == "3":
        calcArea()
    #evaluated, if true the programme is exited (and, therefore, while loop also ends)
    elif x == "q":
        exit()
    #if user input doesn't match any of the above (all if's are false), prints an error message and returns to main menu
    else:
        print("Invalid input: please press [1], [2], [3] or [q] key to select option")
        return

#prints main menu to screen and requests input, which is entered as the parameter in function evalMainMenu 
def inputMainMenu():
    print("\nCalculating Properties of Triangles\nMAIN MENU")
    print("[1] Calculates a missing internal angle of a triangle")
    print("[2] Calculates length of hypotenuse for a right-angled triangle")
    print("[3] Calculates area of a triangle")
    print("[q] Exits programme")
    evalMainMenu(input("\nSelect option and press [Enter] key:"))
    return

#x defines default value for while loop to automatically call main menu function
x = 0
while(x == 0):
    inputMainMenu()