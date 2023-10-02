from CSVHandler import CSVHandler
from legislators import legislators as legislatorsClass

class bills:

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
