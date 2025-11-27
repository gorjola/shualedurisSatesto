import unittest
import employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp1 = employee.Employee("goga", "turadze", 5000)

    def test_email(self):
        self.assertEqual(self.emp1.email, "goga.turadze@mail.com")

    def test_pay_raise(self):
        self.emp1.pay_raise()
        self.assertEqual(self.emp1.pay, 5250)

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "goga_turadze")


if __name__ == "__main__":
    unittest.main()
