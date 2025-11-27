import json


# სტუდენტის ობიექტის შექმნა
class Student:
    def __init__(self, name: str, roll_number: int, grade: float):
        self.__name = name
        self.__roll_number = roll_number
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        self.__grade = new_grade


# სტუდენტის სერვისები
class StudentService:

    # JSON ჩამოტვირთვა
    def load_json(self):
        try:
            with open("Student/students.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    # JSON შენახვა
    def save_json(self, data):
        with open("Student/students.json", "w") as file:
            json.dump(data, file, indent=4)

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
            return "E"

    # grade check (მიღება და ვალიდაცია)
    def grade_input(self):
        grade_check = None
        while grade_check is None:
            try:
                get_grade = float(input("შეიყვანეთ სტუდენტის ქულა (0-100): "))
                if 0 <= get_grade <= 100:
                    grade_check = get_grade
                else:
                    print("გთხოვთ, შეიყვანოთ ქულა 0-100 შუალედში.")
            except ValueError:
                print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვითი მნიშვნელობა (მაგ: 85.5).")
        return get_grade


# ფუნქციები
class StudentFunctions(StudentService):

    def __init__(self):
        super().__init__()

    # სტუდენტის დამატება
    def add_student(self):
        name = input("შეიყვანეთ სტუდენტის სახელი: ")

        get_grade = self.grade_input()
        grade = self.number_to_letter(get_grade)

        data = self.load_json()

        if data:
            new_id = str(max(int(info["roll_number"]) for info in data.values()) + 1)
        else:
            new_id = "1"

        student = Student(name, new_id, grade)

        data[f"student{new_id}"] = {
            "name": student.get_name(),
            "roll_number": student.get_roll_number(),
            "grade": student.get_grade(),
        }

        self.save_json(data)
        print("სტუდენტი წარმატებით დაემატა!")
        input("გაგრძელებისთვის დააჭირეთ Enter...")

    # ყველა სტუდენტის ნახვა
    def load_students(self):
        data = self.load_json()

        if not data:
            print("სტუდენტების სია ცარიელია.")

        for student_id, info in data.items():
            print(
                f"ID: {student_id}, Name: {info['name']}, "
                f"Roll Number: {info['roll_number']}, Grade: {info['grade']}"
            )
        input("გაგრძელებისთვის დააჭირეთ Enter...")

    # სტუდენტის ძებნა roll_number-ით
    def find_student(self):
        data = self.load_json()
        search_id = input("შეიყვანეთ სტუდენტის Roll Number: ")

        for key, i in data.items():
            if str(i["roll_number"]) == search_id:
                print(
                    f"ID: {key}, Name: {i['name']}, "
                    f"Roll Number: {i['roll_number']}, Grade: {i['grade']}"
                )
                input("გაგრძელებისთვის დააჭირეთ Enter...")
                return key
        print("\nსტუდენტი ვერ მოიძებნა.\n")

        cont_option = {
            "1": "გაგრძელება",
            "2": "მთავარ მენიუში დაბრუნება",
        }
        for key, value in cont_option.items():
            print(f"{key}. {value}")
        print("\n")

        choice = input("გთხოვთ აირჩიეთ ოპცია: ")

        if choice == "1":
            return self.find_student()
        else:
            return None

    # მოსწავლის შეფასების განახლება
    def update_grade(self):
        data = self.load_json()
        student_key = self.find_student()

        if student_key:
            get_grade = self.grade_input()
            new_grade = self.number_to_letter(get_grade)

            data[student_key]["grade"] = new_grade
            self.save_json(data)
            print("ქულა წარმატებით განახლდა!")
            input("გაგრძელებისთვის დააჭირეთ Enter...")


# დისპლეი მენიუ
class Display:
    # მენიუს ჩვენება
    def menu(self):
        display_menu = {
            "1": "ახალი სტუდენტის დამატება",
            "2": "ყველა სტუდენტის ნახვა",
            "3": "სტუდენტის ძებნა ნომრის მიხედვით",
            "4": "მოსწავლის შეფასების განახლება",
            "5": "გასვლა",
        }
        print("\n>>> სტუდენტების მართვის სისტემა <<<\n")
        for key, value in display_menu.items():
            print(f"{key}. {value}")
        print("\n")

    # პროგრამის გაშვება
    def run(self):
        service = StudentFunctions()

        while True:
            self.menu()
            choice = input("გთხოვთ აირჩიეთ ოპცია: ")

            if choice == "1":
                service.add_student()
            elif choice == "2":
                service.load_students()
            elif choice == "3":
                service.find_student()
            elif choice == "4":
                service.update_grade()
            elif choice == "5":
                print("პროგრამა დასრულდა.")
                break
            else:
                print("არასწორი არჩევანი, სცადეთ თავიდან.")
                input("\nგაგრძელებისთვის დააჭირეთ Enter...")


# პროგრამის გაშვება
student = Display()
student.run()
