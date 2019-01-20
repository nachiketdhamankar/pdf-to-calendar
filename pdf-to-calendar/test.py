# -*- coding: utf-8 -*-
import datefinder
import datetime
import re

def find_text_between(date1, date2, reverse):
    #print("Recd: ",date1, date2)
    if reverse:
        found = re.search(date2 + ' (.+?) '+ date1, text)
        if found:
            found = found.group(1)
            #print(date2,':', found)

    else:
        found = re.search(date1 + ' (.+?) '+ date2, text)
        if found:
            found = found.group(1)
            #print(date1,':', found)


text = "2019 Sep 4 2019 Wed Ł First day of full-semester and -half fall classes Sep 17 2019 Tue Ł Last day of online class add for full -semester and first-half fall classes Ł Last day to drop a first-half fall class without a W grade Sep 24 2019 Tue Ł Last day to drop a full-semester fall class without a W grade"
text = text.decode('utf-8')
dates_list = []

matches = datefinder.find_dates(text)
for date in matches:
    dates_list.append(date.strftime("%b") + " " + str(int(date.strftime("%d"))) + " " + date.strftime("%Y") + " " + date.strftime("%a"))
    #print(date.strftime("%b") + " " + str(int(date.strftime("%d"))) + " " + date.strftime("%Y"))

print(dates_list)
#find_text_between('Sep 4 2019 Wed', 'Sep 17 2019 Tue')

r_dates_list_itr = reversed(dates_list)

r_dates_list = list(r_dates_list_itr)
#print(r_dates_list)

for date1, date2 in zip(r_dates_list, r_dates_list[1:]):
    print(date1, " : ", date2)
    find_text_between(date1, date2, 1)

for date1, date2 in zip(dates_list, dates_list[1:]):
    #print(date1, " : ", date2)
    find_text_between(date1, date2, 0)
