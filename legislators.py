from CSVHandler import CSVHandler

class legislators:
    def __init__(self):
        self.name = None
        
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

    def get_legislator_name(legislators, legislator_id):
        for legislator in legislators:
            if legislator['id'] == legislator_id:
                return legislator['name']
        return 'Unknown'

    def generate_legislator_csv(_legislators, legislator_votes):
        handler = CSVHandler('legislators-support-oppose-count.csv', ['id', 'name', 'num_supported_bills', 'num_opposed_bills'])
        for legislator_id, votes in legislator_votes.items():
            name = legislators.get_legislator_name(_legislators, legislator_id)
            row = {'id': legislator_id, 'name': name, 'num_supported_bills': votes['num_supported_bills'], 'num_opposed_bills': votes['num_opposed_bills']}
            handler.add_data(row)
        return handler     