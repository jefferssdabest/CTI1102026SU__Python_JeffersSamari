from math import floor
# Samari Jeffers
# 6/28/2026
# This program will take a user input of a dollar amount and 
# return the amount of change in quarters, dimes, nickels, and pennies.
#######################################################################
currency_type = {
    "Dollar":1.00,
    "Quarter":0.25,
    "Dime":0.10,
    "Nickel":0.05,
    "Penny":0.01
}
# Convert decimal to a whole number, using the floor function
#  to prevent floating point errors.
def multiply_by_100(money):
    return floor(money * 100)

# For each currency type, in order,
# store the number of times the respective value (ex. Quarter = 0.25) 
#  can be subtracted from the change amount.
# subtract that which can be subtracted from the change amount.
# add a new entry to the result dictionary containing
# the currency type and number of occurences
# ex. If input is 94.43, the output will be the following:
# {'Dollar': 93, 'Quarter': 1, 'Dime': 1, 'Nickel': 1, 'Penny': 3}
def change_calculator(change, currency_type): 
    result = {} # initialize our result string
    for currency_type, value in currency_type.items():
        currency_int = value * 100
        if currency_int == 1: # handle pennies
            result[currency_type] = int(change)
            continue

        count = change // currency_int
        change -= currency_int * count 
       # print(f"{change} {currency_type} {value}") #debug
        result[currency_type] = int(count)
    return result

# Consider these two functions to pluralize the coin types
# in the output.They were written by ChatGPT when I asked how I might 
# classify the different types of pluralization in English.
# Look how simple and elegant this is. Easily would have taken me
# hours, if not days, to build this on my own. And it would not
#  be nearly as pretty.
# Some lessons to take from this:
# My first mistake was scope creep: I wanted to have a reusable
#  function that would pluralize every word in the English language.
#  Retrospectively, not necessary. 
# Secondly, I did not know about the endswith() method. I would have 
#  used a slice to get the last character and compared it to "y".
#  - A comparable solution, but not as readable.
# Thirdly, I completely forgot that you can use slicing
#  with a colon to get a word without it's last character.
# and no, I would not have written an exception for 1-word
# characters. 

def pluralize(noun):
    if noun.endswith("y"):
        return pluralize_y(noun)
    return noun + "s"

def pluralize_y(noun):
    if len(noun) < 2 or noun[-2] in "aeiou":
        return noun + "s"
    return noun[:-1] + "ies"


# Recursively convert the items in a dictionary into a return summary 
# in the form of a string so that it may be printed cleanly.
#
# ex. if input for original_value is "1.43", and tickets_list is..
# "{'Dollar': 1, 'Quarter': 1, 'Dime': 1, 'Nickel': 1, 'Penny': 3}",
# your result will be the following:

#Change Summary: $1.43 
#-----------
# 1 Dollar
# 1 Quarter
# 1 Dime
# 1 Nickel
# 3 Pennies

def ticket_eater(original_value, tickets_list):
    receipt = f"Change Summary: ${original_value:.2f} \n-----------\n" 
    for coin_type, count in tickets_list.items():
        if count == 0: #do not print coin types that have a count of 0
            continue
        if count != 1: # figure out whether to pluralize or not 
            coin_type = pluralize(coin_type)

        # write to the output, or 'reciept' str
        receipt += f"{count} {coin_type}\n"
    return receipt

###################### DEF MAIN HERE ###############################
# prompt input from the user and calculate how many dollars, 
# quarters, dimes, nickels, and pennies add up to reach
# the submitted number.
def main():
    total = float(input("Enter the amount of money as a float: "))
    times_cien = multiply_by_100(total)
    change = change_calculator(times_cien, currency_type)
    
    print(ticket_eater(total, change))
    if total % 1 == 0:
        print("No Change")
    return 0

# run main() only when called by name
#  useful if you want to try importing this program 
#  and reusing some of the functions within
if __name__ == "__main__":
    main()

