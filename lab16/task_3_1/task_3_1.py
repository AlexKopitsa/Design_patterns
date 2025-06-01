class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class StaffList:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee: Employee):
        self._employees.append(employee)

    def get_iterator(self):
        return StaffListIterator(sorted(self._employees, key=lambda e: e.name))


class StaffListIterator:
    def __init__(self, employees):
        self._employees = employees
        self._position = 0

    def has_next(self):
        return self._position < len(self._employees)

    def next(self):
        if self.has_next():
            employee = self._employees[self._position]
            self._position += 1
            return employee
        else:
            raise StopIteration


if __name__ == "__main__":
    staff = StaffList()
    staff.add_employee(Employee("Olena"))
    staff.add_employee(Employee("Andrii"))
    staff.add_employee(Employee("Bohdan"))

    print("[Employees in alphabetical order]")
    iterator = staff.get_iterator()
    while iterator.has_next():
        print(iterator.next())
