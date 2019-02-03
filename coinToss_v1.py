import random

def coin(): #function that generates either 0 (heads) or 1 (tails)
    r = random.randint(0, 1)
    return r #returns the generated result

choice = input("Enter the choice of the coin side (heads/tails): ")
#print(choice) test if choice is returned correctly
if(choice != "heads" and choice != "tails"): #if input is not as asked
    print("ERROR. Incorrect output, please enter 'heads' or 'tails' only.")
    quit()

r = coin() #assign r as coin() returned variable
#print(r) test if r is returned correctly

if((r == 0 and choice == "heads") or (r == 1 and choice == "tails")): #If statement to decide whether the flip counts as a win or loss
    print("You flipped", choice, "and won. Congratulations!")
else:
        print("You flipped", choice, "and lost. Better luck next time!")
