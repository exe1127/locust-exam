import csv
import os

def listName():
    f = open(r"C:\Users\Exe\Documents\gitHub\locust-exam\listName\name.csv")
    reader = csv.reader(f)
    estruct = []
    for row in reader:
        estruct.append("".join(row))

    return estruct

# print(type(fin))
