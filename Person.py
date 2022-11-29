class Person:
    def __init__(self, person_id: int, first_name: str, last_name: str, sex: str):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
