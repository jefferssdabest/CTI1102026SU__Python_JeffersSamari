from math import floor
import random
# Samari Jeffers
# 7/17/2026
# Generate a random balance for the user to deposit money towards.
# if the balance is paid in full, return the change in dollars, quarters,
#  dimes, and pennies.
# if the user still has balance remaining, prompt the user to deposit more 
#  money, or press 'q' to exit the program
# This builds upon P3LAB1
###############################################################################
# determines the users standing balance
def generate_random_amount():
    return float(round(random.uniform(0.01, 100.00), 2))
# HOW I USED AI FOR THIS:
# I handwrote the first draft of the dispense_change() function, then gave it
#  to ChatGPT and asked it to optimize the code. It came back with several 
#  useful tips:
# * simplify the pluralization logic by defining singular, plural, and
#   in a value together in a listed tuple. No beautiful AI pluralization
#   script here. (referenced in P3Lab1)
#   
# * append looped entries (1 Quarter, 2 Dimes..) to a list and join them 
#   instead of catencating a string. I found the reason why to be quite 
#   instructional, so I'll paraphrase it here:
#      - strings are immutable, so each concatenation creates a new string
#        and copies the existing contents before adding the new text.
#        As the string grows, this repeated copying becomes increasingly
#        expensive.
#      - appending each value to a list avoids repeatedly rebuilding the
#        string. Once all values have been collected, join() allocates the
#        final string once and copies each piece into it, making the overall
#        process much more efficient.
# 
# ChatGPT also reminded me on a seperate query that 
# I misnamed the get_float() function. Before, it was called get_integer.
#
# I then programmed the changes. Everything not mentioned was coded by me.



# check deposit is a valid float and above zero
# if either condition is false, repeat the second prompt until otherwise
# the user can alternatively close the program by pressing 'enter', 'q',
#  or 'exit' at this second prompt.
def get_float():
    num = input("How much cash will you put in the self-checkout? ")
    while True:
        # exit the program if the user enters the following values:
        if num in ["q","exit"]:
            exit()
        try: 
            num = float(num)
            if num >= 0:
                return num
            else:
                print ("This function does not handle negative numbers.")
        except:
            pass

        num = input("Please enter an Integer, or press q to exit: ")


# usage:
# print(dispense_change(1.73))
#
# # outputs: 
# 1 Dollar
# 2 Quarters
# 2 Dimes
# 3 Pennies
def dispense_change(change): 
    currency_type = [
        ("Dollar", "Dollars", 100),
        ("Quarter", "Quarters", 25),
        ("Dime", "Dimes", 10),
        ("Nickel", "Nickels", 5),
        ("Penny", "Pennies", 1)
        ]

    # multiply input by 100 to simplify the math
    # floor resolves repeating decimals.
    times_cien = floor(change * 100)
    output_str = []

    if times_cien % 100 == 0:
        return("No change")

    
    for singular, plural, coin_value in currency_type:
        
        if coin_value == 1: # handle pennies seperately
            if times_cien == 1:
                output_str.append(f"{times_cien} {singular}")
            else:
                output_str.append(f"{times_cien} {plural}")
            continue

        # Figure out how many times our change can divided by a number
        # Then, subtract that from the total amount of change
        count = times_cien // coin_value
        times_cien -= coin_value * count

        # do not write to output if the currency type occurs zero times
        if count == 0:
            continue

        # format answer for all other currency types
        if count == 1:
            output_str.append(f"{count} {singular}")
        else:
            output_str.append(f"{count} {plural}")
            
    return "\n".join(output_str)


def main():
    amount_owed = generate_random_amount()
    while True:
        print(f"You owe ${amount_owed:.2f}")
        deposit = get_float()
        amount_owed = deposit - amount_owed

        # decide if the user has paid off their debts
        # prompt them to try again if not
        if amount_owed < 0:
            amount_owed = abs(amount_owed)
            print(
                f"Contributed ${deposit} to balance.\n"
        "You can continue entering money to deposit, or press 'q' to exit.")
            continue
        else:
            #calculate change
            print(f"Change is: ${amount_owed:.2f}\n")
            print(dispense_change(amount_owed))
            break

if __name__ == "__main__":
    main()



