import json
from datetime import datetime




class Bank:
    def __init__(self, name, lastname, account_num, balance, pin):
        self.name = name
        self.lastname = lastname
        self.account_num = account_num
        self.balance = balance
        self.pin = pin



class Atmservices:
    def __init__(self):
        self.users=self.load_json()

    def log(self, text):
        with open("bankomat1.log", "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def add_user(self):
        try:
            username = input("შეიყვანეთ მომხმარებლის სახელი : ")
            name = input("შეიყვანეთ სახელი : ")
            lastname = input("შეიყვანეთ გვარი : ")
            account_num = int(input("შეიყვანეთ ანგარიშის ნომერი ციფრებით: "))
            balance = float(input("შეიყვვანეთ ბალანსი ციფრებით : "))
            pin = int(input("შეიყვანეთ პინ კოდი ციფრებით: "))
        except ValueError:
            print("შეიყვანეთ სწორი სიმბოლოები")
            return

        user = Bank(name, lastname, account_num, balance, pin)
        self.convent_user(username, user)
        self.save_account()
        print("მომხმარებელი წარმატებით დაემატა")



    def convent_user(self,username: str,user:Bank):
        self.users[username]=user.__dict__

    def save_account(self):
        with open("bank1.json", "w") as file:
            json.dump(self.users, file , indent=4)

    def load_json(self):
        try:
            with open("bank1.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def show_users(self):
        if self.users:
            for user in self.users.items():
                print(user)
        else:
            print("მომხმარებელი არ არსებობს")

    def deposit(self,person, amount):
        if amount > 0:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            person["balance"] += amount
            self.save_account()
            msg=f"{time} Deposited {amount} to {person['lastname']}"
            print(msg)
            self.log(msg)

    def withdraw(self,person, amount):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if 0 < amount <= person["balance"]:
            person["balance"] -= amount
            self.save_account()
            msg=f"{time} Withdrawed {amount} to {person['lastname']}"
            print(msg)
            self.log(msg)
        else:
            print("არარის საკმარისი თანხა")

    def send_money(self,sender,reciver,amount):
        if reciver not in self.users:
            print(f"{reciver} სახელით მომხმარებელი არ არის")
            return
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if 0<amount <= sender["balance"]:
            sender["balance"] -= amount
            self.users[reciver]["balance"] += amount
            self.save_account()
            msg = f"{time} {sender['lastname']} sent {amount} to {self.users[reciver]['lastname']}"
            print(msg)
            self.log(msg)
        else:
            print("არარის საკმარისი თანხა")

    def change_pin(self,person,new_pin):
        person["pin"] = new_pin
        self.save_account()






class AtmMenu:

    def start(self):
        atmservices = Atmservices()

        while True:
            print("\n--- მთავარი მენიუ ---")
            print("1. მომხმარებლის დამატება")
            print("2. მომხმარებლების ნახვა")
            print("3. პირადი კაბინეტი")
            print("4. გამოსვლა")

            choice = input("აირჩიეთ ოფცია : ")

            if choice == "1":
                atmservices.add_user()

            elif choice == "2":
                atmservices.show_users()

            elif choice == "3":
                user = input("შეიყვანეთ მომხმარებლის სახელი: ")

                if user not in atmservices.users:
                    print("მომხმარებელი არ არსებობს!")
                    continue

                try:
                    pin = int(input("შეიყვანეთ პინ კოდი: "))
                except (ValueError, TypeError):
                    print("პინი უნდა იყოს ციფრებით")
                    continue
                person = atmservices.users[user]

                if pin != person["pin"]:
                    print("პინ კოდი არასწორია!")
                    continue

                print(f"Welcome, {person['name']}!")

                # პირადი კაბინეტის მენიუ
                while True:
                    print("\n--- პირადი კაბინეტი ---")
                    print("1. თანხის შეტანა")
                    print("2. ბალანსის ნახვა")
                    print("3. თანხის გამოტანა")
                    print("4. თანხის გაგზავნა")
                    print("5. პინ კოდის შეცვლა")
                    print("6. მთავარ მენიუში დაბრუნება")

                    sub_choice = input("აირჩიეთ ოფცია: ")

                    if sub_choice == "1":
                        try:
                            amount = float(input("შეიყვანეთ თანხა : "))
                            atmservices.deposit(person, amount)
                        except ValueError:
                            print("გთხოვთ შეიყვანოთ მხოლოდ ციფრები")

                    elif sub_choice == "2":
                        print(f"თქვენი ბალანსია : {person['balance']}")

                    elif sub_choice == "3":
                        try:
                            amount = float(input("შეიყვანეთ თანხა : "))
                            atmservices.withdraw(person, amount)
                        except ValueError:
                            print("გთხოვთ შეიყვანოთ მხოლოდ ციფრები")

                    elif sub_choice == "4":
                        try:
                            target = input("შეიყვანეთ მომხმარებელი : ")
                            amount = float(input("შეიყვანეთ თანხა: "))
                            atmservices.send_money(person, target, amount)
                        except ValueError:
                            print("გთხოვთ შეიყვანოთ მხოლოდ ციფრები")

                    elif sub_choice == "5":
                        try:
                            new_pin = int(input("შეიყვანეთ ახალი პინ კოდი : "))
                            atmservices.change_pin(person, new_pin)
                        except ValueError:
                            print("გთხოვთ შეიყვანოთ მარტო ციფრები")


                    elif sub_choice == "6":
                        break

                    else:
                        print("არასწორი ოფცია!")

            elif choice == "4":
                print("კარგად ბრძანდებოდეთ ")
                break

            else:
                print("არასწორი ოფცია!")



meno=AtmMenu()
meno.start()



