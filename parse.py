import csv
import re



with open('budget.csv', 'rb') as budget_csv:
    spamreader = csv.reader(budget_csv, delimiter=",")
    lines = []
    months = []
    rownum = 0
    for row in spamreader:
        if rownum == 0:
            headers = row
            print headers
            if "\xef\xbb\xbf" in headers[0]:
                headers[0] = headers[0].replace('\xef\xbb\xbf', '')
                headers[0] = re.sub('\"', '', headers[0])
            print headers
        else:
            lines.append(row)
            try:
                if row[0] not in months:
                    months.append(row[0])
            except IndexError:
                pass
        rownum += 1

    # for month in months:
    #     for line in lines:
    #         if line[0] == month:
    #             temp = line

class Month(object):

    def __init__(self, month):
        self.month = month
