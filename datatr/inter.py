from datatr.datapath import DATA_PATH
import csv
from numpy import array
print("f")


class GetAfterObj:
    """ this is a class to read and get the data from
    the ready data. path is the path of the csv file .
    you either specify one by yourself or use the
    default case."""

    def __init__(self, path= DATA_PATH):

        self.path = DATA_PATH
        self.data_obj = self.open()

    def open(self):

        with open(self.path, mode="r") as file:

            reader = csv.reader(file)
            arr = array(list(reader))

        file.close()

        yield arr




