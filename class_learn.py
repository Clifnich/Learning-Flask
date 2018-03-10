class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")

#print(player_one.name == player_two.name)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        count = len(self.marks)
        summary = sum(self.marks)
        if not count == 0:
            return summary / count
        else:
            return 0

anna = Student("Anna", "MIT")
anna.marks.append(56)
print(anna.average())

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

anna = WorkingStudent("Anna", "Oxford", 20)
print(anna.salary)

friend = anna.friend("Greg")
print(anna.salary)
