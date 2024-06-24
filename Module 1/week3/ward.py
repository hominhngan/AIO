from abc import abstractmethod


class Person():
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

    def get_yob(self):
        return self._yob


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")
class Ward():
    def __init__(self, name):
        self.__name = name
        self.__people_list = []

    def add_person(self, person):
        self.__people_list.append(person)

    def describe(self):
        print(f"Ward name: {self.__name}")
        for person in self.__people_list:
            person.describe()

    def count_doctor(self):
        num_doctors = 0
        for person in self.__people_list:
            if isinstance(person, Doctor):
                num_doctors += 1
        return num_doctors

    def sort_age(self):
        self.__people_list.sort(key=lambda x: x.get_yob(), reverse=True)
    def compute_average(self):  
        avg = 0.0
        num_teachers = 0
        for person in self.__people_list:
            if isinstance(person, Teacher): #if type(p) is Teacher:
                avg += person.get_yob()
                num_teachers += 1
        return avg / num_teachers

if __name__ == '__main__':
# 2(a)
  student1 = Student(name="studentA", yob=2010, grade="7")
  student1.describe()

  teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
  teacher1.describe()

  doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
  doctor1.describe()
# 2(b)
  print()
  teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
  doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
  ward1 = Ward(name="Ward1")
  ward1.add_person(student1)
  ward1.add_person(teacher1)
  ward1.add_person(teacher2)
  ward1.add_person(doctor1)
  ward1.add_person(doctor2)
  ward1.describe()
# 2(c)
  print(f"\nNumber of doctors: {ward1.count_doctor()}")
# 2(d)
  print("\nAfter sorting Age of Ward1 people")
  ward1.sort_age()
  ward1.describe()

# 2(e)
  print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
# tn
  student1 = Student(name="studentZ2023", yob=2011, grade="6")
  assert student1.get_yob() == 2011
  student1.describe()

  teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
  assert teacher1.get_yob() == 1991
  teacher1.describe() 

  doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologists")
  assert doctor1.get_yob() == 1981
  doctor1.describe()

  student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
  teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
  teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
  doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
  ward1 = Ward ( name =" Ward1 ") 
  ward1.add_person(student1)
  ward1.add_person(teacher1)
  ward1.add_person(teacher2)
  ward1.add_person(doctor1)
  assert ward1.count_doctor() == 1 
  doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
  ward1.add_person(doctor2)
  ward1.count_doctor() #2

       