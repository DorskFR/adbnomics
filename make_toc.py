import csv
import json

toc = []

with open("toc.csv", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for line in csv_reader:
        toc.append({line[0]: line[1]})


with open("toc.json", "w") as f:
    json.dump(toc, f)
