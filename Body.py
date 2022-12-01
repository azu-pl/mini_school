class Person:
    person_id = 1

    def __init__(self, f_name: str, l_name: str, sex: str, person_id: int):
        self.f_name = f_name
        self.l_name = l_name
        self.sex = sex
        self.person_id = person_id

    def __str__(self):
        return f'{self.f_name} {self.l_name} {self.sex} {self.person_id}'


class Student(Person):
    student_id = 1
    index_number = 301

    # grades

    def __init__(self, first_name: str, last_name: str, sex: str, person_id: int,
                 index_number: int, student_id: int, grades=None):

        if grades is None:
            grades = []

        super().__init__(first_name, last_name, sex, person_id)
        self.index_number = index_number
        self.student_id = student_id
        self.grades = grades


    def __str__(self):
        person_s = super().__str__()
        return f'{person_s} {self.index_number} {self.student_id}'

    def to_list(self) -> list:
        return self.__str__().split(' ')

    def add_grade(self, grade):
        if grade in (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0):
            self.grades.append(grade)
            print(self.grades)
        else:
            print("Wrong grade! available grades: 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0 ")


class School:
    school_id = 1

    def __init__(self, school_name: str, school_id: int):
        self.school_name = school_name
        self.school_id = school_id
        self.school_id += 1


class OccupationGroup(School):
    group_id = 1

    def __init__(self, school_name, school_id: int, group_number: int, subject_name: str):
        super().__init__(school_name, school_id)
        self.group_number = group_number
        self.subject_name = subject_name
