import random
import string

hangman = {
    "0" : ("   _____ ",
            "   |   | ",
            "       | ",
            "       | ",
            "       | ",
            "       | ",
            "=======#=="),
    "1" : ("   ____  ",
            "   |   | ",
            "   O   | ",
            "       | ",
            "       | ",
            "       | ",
            "=======#=="),
    "2" : ("   ____  ",
            "   |   | ",
            "   O   | ",
            "  /    | ",
            "       | ",
            "       | ",
            "=======#=="),
    "3" : ("   ____  ",
            "   |   | ",
            "   O   | ",
            "  /|   | ",
            "       | ",
            "       | ",
            "=======#=="),
    "4" : ("   ____  ",
            "   |   | ",
            "   O   | ",
            "  /|\\  | ",
            "       | ",
            "       | ",
            "=======#=="),
    "5" : ("   ____  ",
            "   |   | ",
            "   O   | ",
            "  /|\\  | ",
            "  /    | ",
            "       | ",
            "=======#=="),
    "6" : ("   ____  ",
            "   |   | ",
            "   @   | ",
            "  /|\\  | ",
            "  / \\  | ",
            "       | ",
            "=======#=="),
}

def choose_word(text, min_word_length, max_word_length):
    while True:
        line = random.randint(1,8906)
        word = text[line].upper().rstrip() # rstrip() function remove the "\n"
        if min_word_length <= len(word) < max_word_length:
            return word
        
def choice_level():
    file_name = "english.txt"
    word = None
    with open(file_name, 'r') as file:
        text = file.readlines()
    print("Choose Level below :- ")
    print("Press 'E' for Easy.")
    print("      'M' for Medium.")
    print("      'H' for Hard.")
    while True:
        level = input("level : ").lower()
        if level =='e':
            print(level)
            word = choose_word(text, 4, 6)
            break
        elif level == "m":
            print(level)
            word = choose_word(text, 6, 8)
            break
        elif level == "h":
            print(level)
            word = choose_word(text, 8, 15)
            break
        else:
            print("Invalid level !!!")
            continue
    return word

def game_hint(display_word, word):
    for i in range(len(word)):
        if display_word[i] == "_":
            display_word[i] = word[i]
            break

def display_hangman(life):
    for i in hangman:
            if i == str(life):
                for i in hangman[i]:
                    print(i)

def display_win(word, display_word):
    if ("_" not in display_word):
        print("\nWord is "+word+"")
        print("-"*25)
        print("Conguratulation! You have won.")
        print("-"*25)
        return True
    
def game_over(word):
    print("-"*25)
    for i in hangman["6"]:
        print(i)
    print("Game Over!!!")
    print("\nWord is "+word+"")
    print("-"*25)

def play_game(won):
    word = choice_level()  
    print(word)  
    display_word = ['_'] * len(word)
    word_set = set()
    Good_guess = None
    life = 0
    point = 0
    while life < 6:
        display_hangman(life)
        Good_guess = False
        print(f"\nYou have {6-life} guess.")
        print(*display_word)
        letter = input("Guess a letter (For Hint: Press '1'): ").upper()
        if letter == "1":
            game_hint(display_word, word)
        if letter not in string.ascii_uppercase:
            print("Enter only single alphabet character!")
            continue
        if letter in word_set:
            print("Already Guess")
            continue
        for i in range(len(word)):
            if word[i] == letter:
                word_set.add(word[i])
                display_word[i] = word[i]
                Good_guess = True
        if Good_guess:
            print("Good guess")
        else:
            life += 1
            print("Wrong guess")
        if display_win(word, display_word):
            point += 1
            break
    if life == 6:
        game_over(word)
    won.append(point)

if __name__ == "__main__":
    won = []
    while True:
        play_game(won)
        play_agin = input("Play Again (y/n): ").lower()
        if play_agin == "n":
            break
    print("-------Score Board-------")
    for i, w in enumerate(won):
        print(f"Round {i+1}: {"Win" if w == 1 else "Loose"}")


        
