import csv


def listName():
    f = open("name.csv")
    reader = csv.reader(f)
    estruct = []
    for row in reader:
        estruct.append("".join(row))

    return estruct

# print(type(fin))
