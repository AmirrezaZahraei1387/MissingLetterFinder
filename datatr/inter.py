from datatr.datapath import DATA_PATH
import csv
import time


def openData(path: str = DATA_PATH):

    with open(path, mode='r') as file:
        reader = csv.reader(file)
        reader = list(reader)

    yield reader