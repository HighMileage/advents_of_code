import csv

with open('input_01.txt', 'r') as input_file:
    output = sum(int(value[0]) for value in csv.reader(input_file))
print(output)
