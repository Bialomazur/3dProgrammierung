import unittest
from Employee import Employee

class EmployeeTests(unittest.TestCase):

    def setUp(self):
        self.e1 = Employee(40000, "Maxi", 20, 1.03)
        self.e2 = Employee(70000, "Timo", 28, 1.05)

    def test_check_email(self):

        self.assertEqual(self.e1.email, "Max@PythonModul.com", "Invalid Email Output!")


    def test_salary(self):

        self.assertEqual(self.e1.salary, 40000, "Invalid Salary value!")

    
    def test_salary_increase(self):
        
        self.e1.increase_salary()
        self.e2.increase_salary()

        self.assertEqual(self.e1.salary, 40000 * 1.03, "Invalid Salary increase!")
        self.assertEqual(self.e2.salary, 70000 * 1.05, "Invalid Salary increase!")

    
    def test_age(self):
       
        self.assertEqual(self.e1.age, 20)
        self.assertEqual(self.e2.age, 28)


if __name__ == "__main__":
    unittest.main()




