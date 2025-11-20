import json
from datetime import datetime



class Bank:
    def __init__(self, name, lastname, account, balance, pin):
        self.name = name
        self.lastname = lastname
        self.account = account
        self.balance = balance
        self.pin = pin

    def __repr__(self):
        return f"{self.name} {self.lastname} | {self.account} | Balance: {self.balance}"


    def to_dict(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "account": self.account,
            "balance": self.balance,
            "pin": self.pin
        }


class Bankomat:

    def log(self, text):
        with open("bankomat.log", "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def deposit(self, person, amount):
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if amount > 0:
            person.balance += amount
            msg=f"{time}-->{person.name} შეიტანა {amount}. თქვენი ანგარიში  {person.balance}"
            print(msg)
            self.log(msg)

    def withdraw(self, person, amount):
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if 0 < amount < person.balance:
            person.balance -= amount
            msg=f"{time}-->{person.name} გამოიტანა {amount}. თქვენი ანგარიში :  {person.balance}"
            print(msg)
            self.log(msg)
        else:
            print("არარის საკმარისი თანხა")

    def send_money(self, sender, reciver, amount):
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if 0 < amount < sender.balance:
            sender.balance -= amount
            reciver.balance += amount
            msg = f"{time}-->{sender.name}-იმ გააგზავნა  {amount}  {reciver.name} ის თან , თქვენი ბალანსია  {sender.balance}"
            print(msg)
            self.log(msg)
        else:
            print("არარის საკმარისი თანხა")

    def change_pin(self,person,pin):
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        person.pin = pin
        msg=f"{time}-->{person.name} იმ შეცვალა პინ კოდი , ახალი პინ კოდი არის : {pin}"
        print(msg)
        self.log(msg)






user1=Bank("gio","gorjoladze",4521455441,2000,1111)
user2=Bank("mari","bulia",3521455442,1500,2222)

userslist={
    "user1":user1.to_dict(),
    "user2":user2.to_dict()
}

# marto ertxel gaushvebt ro momxmareblebi sheiqmnas
with open("bank.json","w",encoding="utf-8") as f:
    json.dump(userslist,f,ensure_ascii=False,indent=4)


def load_users():
    with open("bank.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        user={uid:Bank(**info) for uid, info in data.items()}
        return user,data

def save_users(newdata):
    with open("bank.json", "w", encoding="utf-8") as file:
        json.dump(newdata,file,ensure_ascii=False,indent=4)




users,newdata= load_users()
bankomat=Bankomat()



print("**********ბანკომატი**********")

userid=input("შეიყვანეთ მომხმარებლის სახელი :").lower()

if userid not in users:
    print(" მომხმარებელი არ არსებობს")
    exit()

person=users[userid]

userpin=input("შეიყვანეთ მომხმარებლის პინ კოდი :")

if userpin !=str(person.pin):
    print("პინი არასწორია !")
    exit()

print(f"მოგესალმებით {person.name}")

while True:

    print()
    print("1 მომხმარებლის ინფორმაცია")
    print("2 ანგარიშზე თანხის შეტანა")
    print("3 თანხის გამოტანა")
    print("4 გადარიცხვა სხვა მომხმარებელთან")
    print("5 პინ კოდის შეცვლა")
    print("6 გამოსვლა")

    choice=int(input("აირჩიეთ :  "))
    if choice==1:
        print(person)

    elif choice==2:
        bankomat.deposit(person,int(input("შეიყვანეთ თანხა :")))

    elif choice==3:
        bankomat.withdraw(person,int(input("შეიყვანეთ თანხა :")))
    elif choice==4:
        target=input("შეიყვანეთ მომხმარებელი :")
        if target not in users:
            print("მომხმარებელი არ არსებობს")
            continue
        bankomat.send_money(person,users[target],int(input("შეიყვანეთ თანხა :")))
        newdata[target]["balance"]=users[target].balance
    elif choice==5:
        bankomat.change_pin(person,int(input("შეიყვანეთ ახალი პინ კოდი :")))
        newdata[userid]["pin"]=person.pin
    elif choice==6:
        print("კარგად ბრძანდებოდეთ :)")
        break

newdata[userid]["balance"]=person.balance
save_users(newdata)