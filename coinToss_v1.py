import random

def coin():
    """
    A function that randomly generates either 0 or 1
    using the 'random' library and the 'randint' variable
    of the library.
    The result is then returned to the main program.
    """
    r = random.randint(0, 1)
    return r

choice = input("Enter the choice of the coin side (heads/tails): ")
if(choice != "heads" and choice != "tails"): #if input is not as asked, return an error and quit the program.
    print("ERROR. Incorrect output, please enter 'heads' or 'tails' only.")
    quit()

r = coin() #assign r as coin() returned variable

if((r == 0 and choice == "heads") or (r == 1 and choice == "tails")): #If statement to decide whether the flip counts
        print("You flipped", choice, "and won. Congratulations!")       #as a win or loss
else:
        print("You flipped", choice, "and lost. Better luck next time!")
