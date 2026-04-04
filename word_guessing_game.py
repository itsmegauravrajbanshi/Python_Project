import random

def choice_level():
    file_name = "english.txt"
    word = None
    with open(file_name, 'r') as file:
        text = file.readlines()
    while True:
        word_length = int(input("Please enter word length: "))
        if word_length >= 4:
            break
        print("Invalid length!")
    while True:
        line = random.randint(1,8906)
        word = text[line].upper().rstrip() # rstrip() function remove the "\n"
        if len(word) == word_length: 
            break
    return word

def game_hint(display_word, word):
    for i in range(len(word)):
        if display_word[i] == "_":
            display_word[i] = word[i]
            break

def play_game():
    word = choice_level()  
    print(word)  
    display_word = ['_'] * len(word)
    word_set = set()
    Good_guess = False
    while True:
        print(*display_word)
        letter = input("Guess a letter (For Hint: Press '1'): ").upper()
        if letter in word_set:
            print("Already Guess")
        elif letter == "1":
            game_hint(display_word, word)
        else:
            for i in range(len(word)):
                if word[i] == letter:
                    word_set.add(word[i])
                    display_word[i] = word[i]
                    Good_guess = True
            if Good_guess:
                print("Good guess")
            else:
                print("Wrong guess")
        if (display_word == [w for w in word]):
            print("\nWord is "+word+"")
            print("Conguratulation! You have won.")
            break

if __name__ == "__main__":
    play_game()


        
