class Employee:

    def __init__(self, salary, surname, age, salary_increase):
        
        self.salary = salary
        self.surname = surname
        self.age = age
        self.salary_increase = salary_increase


    def increase_salary(self):

        self.salary *= self.salary_increase

    @property
    def email(self):

        return f"{self.surname}@PythonModul.com"

    def __repr__(self):

        return self.surname















