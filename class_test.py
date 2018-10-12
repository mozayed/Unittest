class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # use property decorator
    @property
    def email(self):
        return '{}.{}@mycompany.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


import unittest


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = Employee('John', 'Smith', 50000)
        emp2 = Employee('Linda', 'George', 60000)

        self.assertEqual(emp1.email, 'John.Smith@mycompany.com')
        self.assertEqual(emp2.email, 'Linda.George@mycompany.com')

    def test_fullname(self):
        emp1 = Employee('John', 'Smith', 50000)
        emp2 = Employee('Linda', 'George', 60000)

        self.assertEqual(emp1.fullname, 'John Smith')
        self.assertEqual(emp2.fullname, 'Linda George')

    def test_apply_raise(self):
        emp1 = Employee('John', 'Smith', 50000)
        emp2 = Employee('Linda', 'George', 60000)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.pay, 52500)
        self.assertEqual(emp2.pay, 63000)
