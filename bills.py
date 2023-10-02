from CSVHandler import CSVHandler
from legislators import legislators as legislatorsClass

class bills:

    def count_bill_legislators(votes, vote_results):

        '''
            New function count_bill to avoid nested loop
        '''
        vote_results_dict = {}  # Dict to map results of votes by ID
        for vote_result in vote_results:
            vote_id = vote_result['vote_id']
            legislator_id = vote_result['legislator_id']
            vote_type = vote_result['vote_type']
            
            # Check if ID exists in Dict to avoid duplicates
            if vote_id not in vote_results_dict:
                vote_results_dict[vote_id] = {'supporters': set(), 'opposers': set()}
            
            # Add legislator to category based on vote_type
            if vote_type == '1':
                vote_results_dict[vote_id]['opposers'].add(legislator_id)
            elif vote_type == '2':
                vote_results_dict[vote_id]['supporters'].add(legislator_id)
        
        bill_legislators = {}  # Dict to map count of opositors and not opositors of the law project
        for vote in votes:
            bill_id = vote['bill_id']
            vote_id = vote['id']
            
            # Check vote id to avoid duplicates
            if vote_id in vote_results_dict:
                # Get List of opositors and not opositors to this vote
                supporters = vote_results_dict[vote_id]['supporters']
                opposers = vote_results_dict[vote_id]['opposers']
                
                # Update the counting votes to this project
                if bill_id not in bill_legislators:
                    bill_legislators[bill_id] = {'supporter_count': 0, 'opposer_count': 0}
                
                bill_legislators[bill_id]['supporter_count'] += len(supporters)
                bill_legislators[bill_id]['opposer_count'] += len(opposers)
        
        return bill_legislators


    def generate_bills_csv(bills, bill_legislators, legislators):
        handler = CSVHandler('bills.csv', ['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor'])
        
        for bill in bills:
            bill_id = bill['id']
            title = bill['title']            
            primary_sponsor =  legislatorsClass.get_legislator_name(legislators, bill['sponsor_id'])
            if primary_sponsor == 'Unknown':
                primary_sponsor = 'Unknown'
            supporter_count = bill_legislators[bill_id]['supporter_count']
            opposer_count = bill_legislators[bill_id]['opposer_count']
            row = {'id': bill_id, 'title': title, 'supporter_count': supporter_count, 'opposer_count': opposer_count, 'primary_sponsor': primary_sponsor}
            handler.add_data(row)
        return handler
