import csv
import re

input_file = 'in/people_wiki.csv'
output_file = 'in/pure_people_wiki.csv'
pattern = re.compile(r'%[0-9A-Fa-f]{2}%')

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        if not any(pattern.search(cell) for cell in row):
            writer.writerow(row)