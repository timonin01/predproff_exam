import csv

# открыть

with open('scientists.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

    preparation_date = {}
    scientist_name = {}


def sort_data(data, list):


reader = sort
for ScientistName, preparation, date, components in reader:
    if

with open('scientists.csv', 'scientist_origin', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['ScientistName, preparation, date, components'])
    writer.writerows(reader)
