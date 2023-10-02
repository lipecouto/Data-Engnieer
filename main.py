import csv
from legislators import legislators as legislatorsClass
from bills import bills as billClass

class FileManager:
    __instance = None

    @staticmethod
    def get_instance():
        if not FileManager.__instance:
            FileManager.__instance = FileManager()
        return FileManager.__instance

    def __init__(self):
        self.file_handlers = {}

    def add_handler(self, file_name, handler):
        self.file_handlers[file_name] = handler

    def process_file(self, file_name):
        handler = self.file_handlers.get(file_name)
        if handler:
            handler.process(file_name)
        else:
            print(f"No handler found for file: {file_name}")

def process_files():
    '''
        That is de main function, here the files will be process and the result of this file process will be returned  
    '''
    legislators = []
    bills = []
    votes = []
    vote_results = []

    with open('../legislators.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            legislators.append(row)

    with open('../bills.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bills.append(row)

    with open('../votes.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            votes.append(row)

    with open('../vote_results.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote_results.append(row)
    
    #get results from legislator's counting votes\
    legislator_votes = legislatorsClass.count_legislator_votes(vote_results)

    #generate the legislators csv
    legislator_handler = legislatorsClass.generate_legislator_csv(legislators, legislator_votes)

    #get results from the bill legislators
    bill_legislators = billClass.count_bill_legislators(votes, vote_results)
    
    #generating the bills csv
    bill_handler = billClass.generate_bills_csv(bills, bill_legislators, legislators)

    file_manager = FileManager.get_instance()
    file_manager.add_handler('legislators-support-oppose-count.csv', legislator_handler)
    file_manager.add_handler('bills.csv', bill_handler)
    file_manager.process_file('legislators-support-oppose-count.csv')
    file_manager.process_file('bills.csv')

def main():
    process_files()

if __name__ == '__main__':
    main()
