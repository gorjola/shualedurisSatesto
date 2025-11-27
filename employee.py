class Employee:
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@mail.com"

    @property
    def fullname(self):
        return f"{self.first}_{self.last}"

    def pay_raise(self):
        self.pay = self.pay * self.raise_amount
