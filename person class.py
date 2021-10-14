class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age  = age
        self.gender = gender

    def showInfo(self):
        print("저의 이름은 {0}이고, {1}세{2}입니다.".format(self.name, self.age, self.gender))



obj1 = Person('강현우', 43, '남성')
obj1.showInfo()

class Employee(Person):
    pass

obj2 = Employee("강현우", 26, '남성')
obj2.showInfo()


class Employee(Person):
    def showInfo(self):
        print("저의 이름은 {0}이고, {1}세 {2} 직장인 입니다.".format(self.name, self.age, self.gender))

class Employee(Person):
    def __init__(self, name,age,gender,salary):
        super().__init__(name,age,gender)
        self.salary = salary

    def showInfo(self):
        super().showInfo()
        print("직장인이고, 연봉은{0}입니다.".format(self.salary))

    def doWork(self):
        print("열심히 일합니다.")

class Boss(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age, gender)
        self.employList = []


    def showInfo(self):
        print("사장입니다. employ를 고용할 수 있습니다.")

    def hire(self, employ):
        self.employList.append(employ)

    def makeEmployWork(self):
        for employ in self.employList:
            employ.doWork()

class Prof(Employee):
    def doWork(self):
        print("열심히 가르칩니다.")

class Student(Employee):
    def doWork(self):
        print("열심히 공부합니다.")

class Mananger(Employee):
    def doWork(self):
        print("학생과 교수를 관리합니다.")


obj1 = Prof('강현우', 43, '남성','100만원')

obj2 = Student("강현우", 26, "남성","10만원")

obj3 = Mananger("김미경", 25, '여성','20만원')

boss1 = Boss('김보스', 50, '남성')
boss1.hire(obj1)
boss1.hire(obj2)
boss1.hire(obj3)

boss1.makeEmployWork()
