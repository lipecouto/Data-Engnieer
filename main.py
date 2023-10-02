import csv

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


def count_legislator_votes(vote_results):
    '''
        Counting the votes of legislators, this function expected recive one argument:"vote_results"
    '''
    legislator_votes = {}
    for vote_result in vote_results:
        legislator_id = vote_result['legislator_id']
        vote_type = vote_result['vote_type']
        if legislator_id in legislator_votes:
            if vote_type == '1':
                legislator_votes[legislator_id]['num_opposed_bills'] += 1
            elif vote_type == '2':
                legislator_votes[legislator_id]['num_supported_bills'] += 1
        else:
            if vote_type == '1':
                legislator_votes[legislator_id] = {'num_supported_bills': 0, 'num_opposed_bills': 1}
            elif vote_type == '2':
                legislator_votes[legislator_id] = {'num_supported_bills': 1, 'num_opposed_bills': 0}
    return legislator_votes

def count_bill_legislators(votes, vote_results):
    bill_legislators = {}
    for vote in votes:
        bill_id = vote['bill_id']
        if bill_id not in bill_legislators:
            bill_legislators[bill_id] = {'supporter_count': 0, 'opposer_count': 0}
        
        for vote_result in vote_results:
            if vote_result['vote_id'] == vote['id']:
                legislator_id = vote_result['legislator_id']
                vote_type = vote_result['vote_type']
                if vote_type == '1':
                    bill_legislators[bill_id]['opposer_count'] += 1
                elif vote_type == '2':
                    bill_legislators[bill_id]['supporter_count'] += 1
    return bill_legislators

def get_legislator_name(legislators, legislator_id):
    for legislator in legislators:
        if legislator['id'] == legislator_id:
            return legislator['name']
    return 'Unknown'

def generate_legislator_csv(legislators, legislator_votes):
    handler = CSVHandler('legislators-support-oppose-count.csv', ['id', 'name', 'num_supported_bills', 'num_opposed_bills'])
    for legislator_id, votes in legislator_votes.items():
        name = get_legislator_name(legislators, legislator_id)
        row = {'id': legislator_id, 'name': name, 'num_supported_bills': votes['num_supported_bills'], 'num_opposed_bills': votes['num_opposed_bills']}
        handler.add_data(row)
    return handler

def generate_bills_csv(bills, bill_legislators, legislators):
    handler = CSVHandler('bills.csv', ['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor'])
    for bill in bills:
        bill_id = bill['id']
        title = bill['title']
        primary_sponsor = get_legislator_name(legislators, bill['sponsor_id'])
        if primary_sponsor == 'Unknown':
            primary_sponsor = 'Unknown'
        supporter_count = bill_legislators[bill_id]['supporter_count']
        opposer_count = bill_legislators[bill_id]['opposer_count']
        row = {'id': bill_id, 'title': title, 'supporter_count': supporter_count, 'opposer_count': opposer_count, 'primary_sponsor': primary_sponsor}
        handler.add_data(row)
    return handler

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
    
    #get results from legislator's counting votes
    legislator_votes = count_legislator_votes(vote_results)
    
    #generate the legislators csv
    legislator_handler = generate_legislator_csv(legislators, legislator_votes)

    #get results from the bill legislators
    bill_legislators = count_bill_legislators(votes, vote_results)
    
    #generating the bills csv
    bill_handler = generate_bills_csv(bills, bill_legislators, legislators)

    file_manager = FileManager.get_instance()
    file_manager.add_handler('legislators-support-oppose-count.csv', legislator_handler)
    file_manager.add_handler('bills.csv', bill_handler)
    file_manager.process_file('legislators-support-oppose-count.csv')
    file_manager.process_file('bills.csv')

def main():
    process_files()

if __name__ == '__main__':
    main()
