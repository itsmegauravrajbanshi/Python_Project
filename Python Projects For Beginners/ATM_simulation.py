from datetime import datetime

Bank_database = { 
    "Users" : 
        [
            {   
                "pin_no" : "1234",
                "Account_no" : "12345678",
                "full_name" : "Prem Rajbanshi", 
                "Balance_amt" : 0
            },
            {   
                "pin_no" : "1235",
                "Account_no" : "12345690",
                "full_name" : "Malati Rajbanshi", 
                "Balance_amt" : 0
            },
            {   
                "pin_no" : "1236",
                "Account_no" : "12345660",
                "full_name" : "Ganesh Wagle", 
                "Balance_amt" : 0 
            },
            { 
                "pin_no" : "1237",
                "Account_no" : "12345699",
                "full_name" : "Shyam Sundar", 
                "Balance_amt" : 0
            }
        ]
}
class ATM:
    def __init__(self):
        self.history_lst = []

    def check_balance(self, user : str) -> str:
        print("*"*30)
        print(f"Current Balance : {user['Balance_amt']}")
        print(f"Available Balance : {user['Balance_amt']}")
        print("*"*30)
        return f"Current Balance : {user['Balance_amt']}\n" + f"Available Balance : {user['Balance_amt']}\n"

    def deposit(self, user : str) -> str:
        deposit_amt = int(input("Enter Deposit amount: "))
        message = ""
        print("*"*30)
        if deposit_amt > 0:
            user["Balance_amt"] += deposit_amt 
            print("Deposited Successfully!!")
            message = f"Amount {deposit_amt}, Deposited Successfully!!"
        else:
            print("Invalid Amount...!")
            print("Transaction Failed.")
            message = "Invalid Amount...!\nTransaction Failed"
        print(f"Available Balance : {user['Balance_amt']}")
        return message + f"\nAvailable Balance : {user['Balance_amt']}\n"
    
    def withdraw(self, user : str) -> str:
        message = ""
        withdraw_amt = int(input("Enter withdraw amount: "))
        print("*"*30)
        balance = user['Balance_amt']
        if 0 < withdraw_amt < balance:
            user["Balance_amt"] -= withdraw_amt
            print("Withdrawn Successfully!!")
            message = f"Amount {withdraw_amt}, Withdrawn Successfully!!"
        elif withdraw_amt < 0:
            print("Invalid Amount...!")
            print("Transaction Failed.")
            message = "Invalid Amount...!\nTransaction Failed"
        else:
            print("Insufficent Balance....!")
            print("Transaction Failed.")
            message = "Insufficent Balance...!\nTransaction Failed"
        print(f"Available Balance : {user['Balance_amt']}")
        print("*"*30)
        return message + f"\nAvailable Balance : {user['Balance_amt']}\n"

    def check_pin(self) -> str:
        attemps : int = 3
        current_user : str | None = None

        while attemps > 0:
            pin_no : str = input("Enter PIN : ")
            if len(pin_no) != 4:
                print("Enter 4 digit only")
                continue

            for user in Bank_database["Users"]:
                if user["pin_no"] == pin_no:
                    current_user = user
                    break
            
            if current_user == None:
                print(f"Invalid Pin! {attemps-1} attemps left.")
                attemps -= 1
                continue
            else:
                break
        return current_user

    def display_menu(self) -> None:
        print("*"*30)
        print("|    Welcome to the ATM!     |")
        print("*"*30)
        print("| 1. Check Balance           |")
        print("| 2. Deposit                 |")
        print("| 3. Withdraw                |")
        print("| 4. Show Transaction        |")
        print("| 5. Exit                    |")
        print("*"*30)


    def show_history(self):
        print("*"*30)
        print("|    Transaction history     |")
        print("*"*30)
        if not self.history_lst:
            print("No Transaction Found..!")
        else:
            # with open("Record.txt", 'r') as file:
            #     lines = file.readlines()
            # for line in lines:
            #     print(line, end="\n")
            for index, data in enumerate(self.history_lst):
                print(f"{data}")
             
if __name__ == "__main__":
    atm = ATM()
    current_user = atm.check_pin()
    if current_user == None:
        exit()
    else:
        atm.history_lst.append(f"Login time :{datetime.now()}")
    while True:
        atm.display_menu()
        choice = input("Please enter an option: ")
        if choice == "1":
            message = atm.check_balance(current_user)
            atm.history_lst.append(message)   
        elif choice == "2":
            message = atm.deposit(current_user)
            atm.history_lst.append(message)
        elif choice == "3":
            message = atm.withdraw(current_user)
            atm.history_lst.append(message)
        elif choice == "4":
            atm.show_history()
            input("Press 'Enter' to continue.. ")
        else:
            atm.history_lst.append(f"Logout time :{datetime.now()}")
            # with open("Record.txt", 'w') as file:
            #     file.writelines(atm.history_lst)
            break

