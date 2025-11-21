class Student:
    def __init__(self, name="", age=0, grade=""):
        self.name = name
        self.age = age
        self.grade = grade

    def number_to_letter(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def new_student(self):
        pass

    def view_students(self):
        pass

    def find_student(self):
        pass

    def update_grade(self):
        pass

    def menu(self):
        display_menu = {
            "1": "ახალი სტუდენტის დამატება",
            "2": "ყველა სტუდენტის ნახვა",
            "3": "სტუდენტის ძებნა ნომრის მიხედვით",
            "4": "მოსწავლის შეფასების განახლება",
            "5": "გასვლა",
        }
        for key, value in display_menu.items():
            print(f"{key}. {value}")

    def run(self):
        while True:
            self.menu()
            choice = input("გთხოვთ აირჩიეთ ოპცია: ")

            if choice not in ["1", "2", "3", "4", "5"]:
                print("არასწორი არჩევანი, გთხოვთ სცადოთ თავიდან.")
                continue

            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                print("პროგრამა დასრულდა.")
                break


student = Student()
student.run()
