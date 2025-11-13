class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary

    def set_salary(self, new_salary, setter):
        if isinstance(setter, HR):
            self.__salary = new_salary
            print(f"{self.name} uchun yangi ish haqi belgilandi: {self.__salary}")
        else:
            print("Xato: faqat HR xodimi ish haqini o‘zgartira oladi.")

    def get_salary(self, requester):
        if isinstance(requester, Manager):
            return self.__salary
        else:
            return "maxfiy"

    def get_info(self):
        return f"Ism: {self.name}, Lavozim: {self.position}"


class Manager(Employee):
    def __init__(self, name, salary=0):
        super().__init__(name, "Manager", salary)


class HR(Employee):
    def __init__(self, name, salary=0):
        super().__init__(name, "HR", salary)


emp1 = Employee("Behruz", "Dasturchi", 5000)
manager = Manager("Gulguncha", 7000)
hr = HR("Ozodbek", 6000)

emp1.set_salary(5500, hr)

print("Manager ko‘radi:", emp1.get_salary(manager))

print("Oddiy xodim ko‘radi:", emp1.get_salary(emp1))
