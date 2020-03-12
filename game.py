# Create an array of case values
# Create an empty array to hold the user’s first case
# Create an array to hold visible cases
# Start:

# Move 1 case to userCase
# Each Turn:
# Generate a banker’s offer which is a currency #, avg of remaining case values.
# Advance play with keystroke:
# Move random 6 (then 5, 4..etc) cases to visible array
# User can choose banker’s offer
# User can choose their own chosen case
# User can see quantity of hidden cases
# Display visible array
# userCase = []
# caseVisible = []
# caseValues = [$.01, $1, $5, $10, $25, $50...
import random
import math

case_values = [.01 , 1 , 5 , 10 , 25 , 50 , 75 , 100 , 200 , 300 , 400 , 500 , 750 , 1000 , 5000 , 10000 , 25000 , 50000 , 75000 , 100000 , 200000 , 300000 , 400000 , 500000 , 750000 , 1000000]
user_case = []
case_visible = []
REMOVE_NUMBER = 6
win = False
    
def game_setup():
    first_case = random.choice(case_values)
    user_case.append(first_case)
    case_values.remove(first_case)

def case_remove():
    global REMOVE_NUMBER
    remove_cases = random.sample(case_values, k=REMOVE_NUMBER)
    for case in remove_cases:        
        case_visible.append(case)
        case_values.remove(case)
    if REMOVE_NUMBER > 1:
        REMOVE_NUMBER-=1
    
def generate_offer():
    offer = math.floor(sum(case_values)/len(case_values))
    return offer

def game_play():
    global win
    global case_visible
    game_setup()
    case_remove()
    offer = generate_offer()
    while win == False:
        amount_remaining_cases = len(case_values)
        print(f"Removed Cases: {case_visible} Cases Remaining: {amount_remaining_cases}")
        print(f"Bankers Offer: {offer}")
        print("Choose 1 to take banker's offer")
        print("Choose 2 to take your chosen case")
        print("Choose 3 to remove more cases")
        choice = input("Enter your value: ")
        if choice == 3:
            case_remove()
            generate_offer()
        elif choice == 2:
            win = True
        elif choice == 1:
            win = True

game_play()


