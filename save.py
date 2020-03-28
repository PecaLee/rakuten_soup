import csv

def save_to_file(goods):
    file = open("goods.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title","price","link"])
    for good in goods:
        writer.writerow(list(good.values()))
    return