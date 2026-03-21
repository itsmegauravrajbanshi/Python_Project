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

def search_and_replace():
    with open(file_name, 'r')as file:
        content = file.read()
        print(content)
        while True:
            old_text = input("Search text: ")
            if old_text in content:
                replace_text = input("Replace text: ")
                content = content.replace(old_text, replace_text)
                with open(file_name, 'w')as file:  
                    file.write(content)
                    print("Replaced successfully")
                break
            else:
                print("Text not found. Try Again!!!")
             
def text_function():
    while True:
        print("1. Overwrite the file \n2. Append new text. \n3. Search and Replace \n4. Exit")
        try:
            choice = int(input("Enter choice (1-4):"))
            if choice == 1:
                file_mode(WRITE)
                continue
            elif choice == 2:
                file_mode(APPEND)
                continue
            elif choice == 3:
                search_and_replace()
            elif choice == 4:
                break
            else:
                print("Enter correct choice!!!")
        except ValueError as ve:
            print("Enter number only!!!")

def file_mode(mode):
    print("Enter your text (type 'SAVE' on a new line to save and exit or 'EXIT' to exit without save.):")
    text, signal = join_text()
    if signal:
        with open(file_name,mode) as file:
            file.write(text)
            print(f"File {file_name} saved.")
    else:
        print(f"File {file_name} doesn't saved." )

def is_file_exist():
    if Path(file_name).is_file():
        print(f"{file_name} found.")
        text_function()
    else:
        print(f"{file_name} not found. Creating a new file..")        
        open(file_name,APPEND).close()
        file_mode(APPEND)

if __name__ == '__main__':
    file_name = input("Enter the filename to open or create: ")
    is_file_exist()

    