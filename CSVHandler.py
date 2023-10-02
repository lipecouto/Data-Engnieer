import csv

class CSVHandler:
    '''
        this Class will be handle with the CSV files
    '''
    def __init__(self, output_file, fieldnames):
        self.output_file = output_file
        self.fieldnames = fieldnames
        self.data = []

    def add_data(self, row):
        self.data.append(row)

    def process(self, file_name):
        with open(self.output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.data)