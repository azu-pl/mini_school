from Body import Student
from CSVManager import CSVManager
from faker import Faker
import random

fake = Faker()
people_database = 'people_list.csv'
options = {
    'add': 'Add new student',
    'show': 'Show student list',
    'exit': 'Exit an application'
}


is_running = True

if __name__ == '__main__':

    while is_running:
        option = input(f'Please choose option: {options}\n').lower()

        if option not in options.keys():
            print('Wrong option. Please type:')
            for key, value in options.items():
                print(f'{key} - {value}')
        elif option == 'add':
            with open(people_database) as f:
                increment = sum(1 for line in f)
            s = Student(fake.first_name(),
                        fake.last_name(),
                        random.choice(["male", "female"]),
                        Student.person_id + increment,
                        Student.index_number + increment,
                        Student.student_id + increment

                        )

            with CSVManager(people_database, 'a+') as csvm:
                csvm.writerow(s.to_list())
                print('Student added to db.')

        elif option == 'show':
            with CSVManager(people_database, 'r+') as csvm:
                for row in csvm:
                    print(row)

        elif option == 'exit':

            is_running = False
