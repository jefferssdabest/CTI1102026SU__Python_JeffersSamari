# Samari Jeffers
# 6/14/2026
# P1HW1
# perform math operations from user input

def printHeader(header):
    print(f"----{header}----\n\n")
    return

# Ask the user for input, then asks again if the input is not an integer.
def getInteger(prompt):
    while True: 
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")
            

def calcExponents():
    BASE_NUM = getInteger("Enter a integer as the base value: ")
    EXP_NUM = getInteger("Enter a integer as the exponent: ")
    print("\n") # two spaces
    PRODUCT = BASE_NUM ** EXP_NUM
    print (f"{BASE_NUM} raised to the power of {EXP_NUM} is {PRODUCT} !!\n\n")
    return


def addAndSubtract():
    NUM1 = getInteger("Enter a starting integer: ")
    NUM2 = getInteger("Enter an integer to add: ")
    NUM3 = getInteger("Enter an integer to subtract: ")
    print("\n") # two spaces

    PRODUCT = (NUM1 + NUM2) - NUM3
    print(f"{NUM1} + {NUM2} - {NUM3} is equal to {PRODUCT}\n\n")
    return



printHeader("Calculating Exponents")
calcExponents()
printHeader("Addition and Subtractions")
addAndSubtract()

# Keeps the window open
input("Press enter to continue.... ")
