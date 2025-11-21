import json


class Student:
    def __init__(self, name="", age=0, grade=""):
        self.name = name
        self.age = age
        self.grade = grade


class StudentServices:
    # გადაყავს ქულები ასოებად
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

    # ახალი სტუდენტის დამატება
    def new_student(self):
        name = input("შეიყვანეთ სტუდენტის სახელი: ")
        age = int(input("შეიყვანეთ სტუდენტის ასაკი: "))
        total = 0
        for i in range(1, 4):
            grade = int(input(f"სტუდენტის შეფასება N{i}: "))
            total += grade
        num_to_char = self.number_to_letter(total)
        student = Student(name, age, num_to_char)

        with open("Student/students.json", "r+") as file:
            data = json.load(file)

            if data["students"]:
                new_id = str(max(int(i) for i in data["students"].keys()) + 1)
            else:
                new_id = "1"

            data["students"][new_id] = {
                "name": student.name,
                "age": student.age,
                "grade": student.grade,
            }

            file.seek(0)
            json.dump(data, file, indent=4)

        print("სტუდენტი წარმატებით დაემატა!")
        return student

    # ყველა სტუდენტის ნახვა
    def view_students(self):
        with open("Student/students.json", "r") as file:
            data = json.load(file)
            for student_id, info in data["students"].items():
                name = str(info["name"])
                age = str(info["age"])
                grade = str(info["grade"])
                student_id_str = str(student_id)

                print(
                    f"ID: {student_id_str}, სახელი: {name}, ასაკი: {age}, ქულა: {grade}"
                )

    # სტუდენტის ძებნა id მიხედვით
    def find_student(self):
        pass

    # მოსწავლის შეფასების განახლება
    def update_grade(self):
        pass

    # მენიუს ჩვენება
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

            elif choice == "1":
                self.new_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                print("პროგრამა დასრულდა.")
                break


service = StudentServices()
service.run()
