# Ask roll the dice
# if yes, roll two dice and print the result
# if no, print "Thanks for playing. Goodbye!" and exit the program
# else print invalid choice.

import random
# def Dice():
#     dice = random.randint(1, 6)
#     return (dice)

def Roll_Dice(num_dice):
    dice_lst = [random.randint(1, 6) for i in range(num_dice)]
    return dice_lst
    
if __name__ == "__main__":
    print("Welcome to the Dice Roller!")
    answer = input("Roll a dice? (y/n)").lower()
    count = 0   
    while True:
        roll_dice = int(input("How many dice(1-8) do you want to roll?"))
        if answer == 'y' and 1 <= roll_dice <= 8:
            print(Roll_Dice(roll_dice))
            if count > 0:
                print ("How many times you have rolled the dice./n Press '1' to check or 'Any key' to skip.")
                if input() == '1':
                    print(f"You have rolled the dice {count} times.")
            answer = input("Roll again? (y/n)").lower()
            if answer == 'n':
                print("Thanks for playing. Goodbye!")
                break     
        elif answer == 'n':
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
        count += 1
        

