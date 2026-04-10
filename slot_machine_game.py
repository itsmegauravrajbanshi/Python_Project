import random

def display_slot():
    symbol = [
        '🍉','🔔','🍊','🍋','🍌','🪙',
        '🎁','🍒','💎','🎱','🏇','🏦',
        '⭐','💰','💣','💴','💵','💶',
        '🧾','💷','💸','🌟','💳','🎲',
        '☘️ ','🤑','🍀']
    slot = [random.randrange(len(symbol)) for _ in range(3)]
    print("*"*12)
    print(symbol[slot[0]],"|", symbol[slot[1]],"|", symbol[slot[2]])
    print("*"*12)
    return slot

def display_balance(current_balance, bet_amt):
    win_amt = 0
    slot = display_slot()
    if slot[0] == slot[1] == slot[2]:
        win_amt = bet_amt * 10
        print(f"Congratulation! You have won {win_amt}")
    elif slot[0] == slot[1] or \
        slot[0] == slot[2] or\
        slot[1] == slot[2]:
        win_amt = bet_amt * 2
        print(f"You won {win_amt}! 2x of your bet")
    else:
        current_balance -= bet_amt
        print(f"You lose {bet_amt}")
        
    return current_balance + win_amt

if __name__ == "__main__":
    current_balance = int(input("Enter your starting balance: "))
    print("\nWelcome to Slot Machine Game!")
    print(f"You start with a balance of {current_balance}")

    while current_balance > 0:
        print(f"\nCurrent Balance: {current_balance}")
        bet_amt = input("Enter your bet amount: ")

        if not bet_amt.isdigit():
            print("Invalid amount!")
            continue

        current_balance = display_balance(current_balance, int(bet_amt))
        print(f"Remaining balance: {current_balance}")

        if current_balance == 0:
            print("Insufficent Balance!!!")
            break

        play_again = input("Do you want to play again? (y/n) :")
        if play_again == 'n':
            break
        