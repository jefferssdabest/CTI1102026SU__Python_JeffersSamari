# Samari Jeffers
# 6/14/2026
# P1HW2
# Calculate and display travel expenses from user input
#######################################################################
# Format: (prompt, data type, label)
questions = (
("Enter budget: ", int, "BUDGET"), 
("Enter your travel destination: ", str, "LOCATION"), 

("How much do you think you will spend on gas? ", int, "Fuel"),
("How much will you need for accomodation/hotel? ", int, "Accomodation"),
("Last, how much do you need for food? ", int, "Food")

)
#PSUEDOCODE:
#
# Here's a list of questions to ask, what values to expect, and a
# label to bind them to.
#
# For each question:
# Check that the expected data type is not an integer
#   otherwise, use the input function to gather raw input from the user.
#   store that info in a dictionary with the provided label.
#
#  Otherwise, attempt to classify the users input as an integer
#     if that fails, respond "Invalid input. Please enter an integer."
#     ask again until the provided input is an integer.
#     store that info in a dictionary with the provided label.
# 
# With the new data, set aside the entries labeled "BUDGET" and 
# "LOCATION" and store them into seperate values. 
# Subtract each following data point from the value defined in "BUDGET"
# and store that value as "TOTAL"
#
# Finally, display the BUDGET, LOCATION, (*expenses), and TOTAL in a
# preformatted message.

# THIS FUNCTION IS RESPONSIBLE FOR SOLICITING INFO FROM THE USER
#
# Iterate through questions and create prompts for the user
#
# 
# returns the result in the following format:
# {'BUDGET': INT, 'LOCATION: STR', 'LABEL': INT, 'LABEL': INT, ...}
def ticketEater():
    output = {}
    for prompt, data_type, label in questions:

        # dont enforce input thats not marked as int
        if (data_type != int):
            output[label] = input(prompt)
            continue

        # get integers from the user and reject invalid input
        while True: # repeat until they get it right
            try:
                output[label] = int(input(prompt))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    return output


# Take output from ticketEater() and calculate the budget 
def getTotal(BUDGET,RECIEPT):
    subtractants = RECIEPT 
    whats_left = BUDGET

    for expense in subtractants.values():
       whats_left = ((whats_left - expense))
    return whats_left


def displayBudgetSummary(LOCATION,BUDGET,RECIEPT,TOTAL):

    print(f"------------Travel Expenses------------")
    print(f"Location: {LOCATION}")
    print(f"Initial Budget: {BUDGET}\n")
   
    for LABEL, VALUE in RECIEPT.items():
        print(f"{LABEL}: {VALUE}")


    print(f"\nRemaining Balance: {TOTAL}")

    return

def main():

    RECIEPT = ticketEater()
    LOCATION = RECIEPT.pop("LOCATION")
    BUDGET = RECIEPT.pop("BUDGET")

    TOTAL = getTotal(BUDGET, RECIEPT)

    displayBudgetSummary(LOCATION,BUDGET,RECIEPT,TOTAL)
    return

main()
# keep the window open
input("Press enter to continue.... ")


            


