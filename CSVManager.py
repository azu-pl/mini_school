import csv


class CSVManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.file_handler = None

        if mode in ['w+', 'w', 'a', 'a+']:
            self.mode = 'a+'

        if mode in ['r', 'r+']:
            self.mode = 'r+'

    def __enter__(self):
        self.file_handler = open(self.file_name, self.mode, newline='\n')

        if self.mode == 'r+':
            return csv.reader(self.file_handler, delimiter=';')
        else:
            return csv.writer(self.file_handler, delimiter=';')

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_name, 'r') as file_to_count:
            print(f'People Counter: {len(file_to_count.readlines())}')
        self.file_handler.close()
