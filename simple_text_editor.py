from pathlib import Path
APPEND = 'a'
WRITE = 'w'

def join_text():
    lines = []
    signal = None
    while True:
        line = input()
        if line.upper() == "SAVE":
            signal = True 
            break
        elif line.upper() == "EXIT":
            signal = False
            break
        lines.append(line)
    return "\n".join(lines), signal
        
def text_function():
    while True:
        print("1. Overwrite the file \n2. Append new text")
        try:
            choice = int(input())
            if choice == 1:
                file_mode(WRITE)
                break
            elif choice == 2:
                file_mode(APPEND)
                break
            else:
                print("Enter correct choice.")
        except ValueError as ve:
            print("Enter number only.")

def file_mode(mode):
    print("Enter your text (type 'SAVE' on a new line to save and exit or 'EXIT' to exit without save.):")
    text, signal = join_text()
    if signal:
        with open(file_name,mode) as file:
            file.write(text)
            print(f"File {file_name} saved.")
    else:
        print(f"File {file_name} doesn't saved." )

file_name = input("Enter the filename to open or create: ")

if Path(file_name).is_file():
    print(f"{file_name} found.")
    text_function()
else:
    print(f"{file_name} not found. Creating a new file..")        
    open(file_name,APPEND).close()
    file_mode(APPEND)

    