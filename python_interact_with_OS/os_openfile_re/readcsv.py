import csv

with open('python_interact_with_OS/software.csv', encoding='utf-8-sig') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))
