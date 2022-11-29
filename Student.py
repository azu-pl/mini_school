from Person import Person


class Student(Person):
    def __init__(self, person_id: int, first_name: str, last_name: str, sex: str, student_id: int, index_number: int):

        super().__init__(person_id, first_name, last_name, sex)
        self.student_id = student_id
        self.index_number = index_number
