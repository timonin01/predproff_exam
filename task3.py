import csv

# открыть

with open('scientists.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

for ScientistName, preparation, date, components in reader:
    while input() != 'эксперемент':
        data = input().split('-')
        year2, month2, day2 = date.split('-')
        if data == date:
    else:
        print()
