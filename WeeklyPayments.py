import csv

def WeeklyPayments(a,b): # Weekly report= a, Salesforece report = b
    #create a dict from first csv, with clearing solution id as key
    with open("a", "rb") as f:
        first = {rows[0]: rows[3:] for rows in list(csv.reader(f))}

    # compare second csv, append rank, add received recurring columns
    with open("b", "rb") as f:
        for row in csv.reader(f):
            if row and row[0] in first:  # row[0] = clearing solution id
                first[row[0]].append(row[1])  # row[1] = rank
                first[row[0]].append(row[2])
                first[row[0]].append('Received')
                first[row[0]].append('Recurring')


    # convert dict back to list
    merged = [tuple(v) for k, v in first.items()]

    # write list to output csv
    with open('Weekly DDS PAYMENT UPLOADS.csv', "w") as f:
        writer = csv.DictWriter(f, fieldnames=['Payment Date', 'Payment Amount', 'Opportunity ID','Account ID', 'Payment Status', 'Payment Type'], lineterminator='\n')
        writer.writeheader()
        csv.writer(f, lineterminator='\n').writerows(merged)











