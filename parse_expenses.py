import csv
import re
from pprint import pprint




with open('expenses.csv', 'rb') as budget_csv:
    spamreader = csv.reader(budget_csv, delimiter=",")
    data = []

    for row in spamreader:
        if "Total" not in row[0]:
            if row[1]:
                data.append(row[0])
    # months_list = []
    # cata_list = []
    # master_catagory_list = []
    # sub_catagory_list = []
    # rownum = 0
    # for row in spamreader:
    #     if rownum == 0:
    #         headers = row
    #         #print headers
    #         if "\xef\xbb\xbf" in headers[0]:
    #             headers[0] = headers[0].replace('\xef\xbb\xbf', '')
    #             headers[0] = re.sub('\"', '', headers[0])
    #         print headers
    #     else:
    #         data.append(row)
    #     rownum += 1

    # for row in data:
    #     try:
    #         if row[mon_idx] not in months_list:
    #             months_list.append(row[mon_idx])
    #         cat = row[cata_idx].split(':')[0]
    #         sub = row[cata_idx].split(':')[1]
    #         if cat not in master_catagory_list:
    #             master_catagory_list.append(cat)
    #         if sub not in sub_catagory_list:
    #             sub_catagory_list.append(sub)

    #     except IndexError:
    #         pass

    pprint(data)
    # pprint(master_catagory_list)
    # pprint(sub_catagory_list)
    # for month in months_list:
    #     for line in lines:
    #         if line[0] == month:
    #             temp = line


class Month(object):

    def __init__(self, month):
        self.month = month
