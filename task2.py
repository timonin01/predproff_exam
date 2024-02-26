import csv

# открыть

with open('scientists.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]
def sort_data(data,list):
