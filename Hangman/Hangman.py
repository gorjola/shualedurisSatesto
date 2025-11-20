import json
import random

"""
Hangman არის სიტყვების გამოცნობის თამაში. პროგრამა ირჩევს შემთხვევით სიტყვას წინასწარ განსაზღვრული სიიდან
და აჩვენებს მას ქვედა ტირეების გამოყენებით (რამდენი ასოცაა სიტყვაში, იმდენი ქვედა ტირე), რომელიც წარმოადგენს
ფარულ ასოებს. მომხმარებლებს სთხოვენ გამოიცნონ ასო და პროგრამა ამოწმებს არის თუ არა ასო სიტყვაში. ვლინდება სწორად 
გამოცნობილი ასოები და თამაში გრძელდება მანამ, სანამ მომხმარებელი არ გამოიცნობს სიტყვას ან არ ამოიწურება
მცდელობები.
"""


class Hangman:
    def __init__(self, word_list, life=3):
        self.word_list = word_list
        self.life = life

    # სიტყვების შემთხვევითი არჩევა
    def get_random_word(self):
        return random.choice(self.word_list)

    # თამაშის ლოგიკა
    def play(self):
        chosen_word = self.get_random_word()
        separated_word = list(chosen_word)
        hidden_word = ["_"] * len(chosen_word)

        while self.life > 0:
            print(" ".join(hidden_word))
            user_input = input("შეიყვანეთ ასო: ").lower()

            # ვალიდაცია
            if len(user_input) != 1:
                print("გთხოვთ შეიყვანოთ მხოლოდ ასო")
                continue
            elif not ("\u10d0" <= user_input <= "\u10f0"):
                print("გთხოვთ შეიყვანოთ ქართული ასო")
                continue
            elif not user_input.isalpha():
                print("გთხოვთ შეიყვანოთ მხოლოდ ასოები")
                continue

            # ასოების შემოწმება
            if user_input in separated_word:
                for i, letter in enumerate(separated_word):
                    if letter == user_input:
                        hidden_word[i] = user_input
                print(f"თქვენ გამოიცანით ასო: {user_input}, {hidden_word}")
            else:
                self.life -= 1
                print(
                    f"ასობგერა {user_input} ვერ მოიძებნა. დაგრჩათ {self.life} სიცოცხლე."
                )

            if "_" not in hidden_word:
                print("გილოცავ! გამოცნობილი სიტყვაა:", chosen_word)
                return

        print("სამწუხაროდ თქვენ წააგეთ, სწორი პასუხი იყო:", chosen_word)


with open("hangman/words.json", "r") as file:
    data = json.load(file)
    words = data["words"]


game = Hangman(words)
game.play()
