from datapath import DATA_PATH
import csv
from numpy import array


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

    def startsWE(self, part_sp):
        """this function will get the value part_sp
        and will return the possible values that can go
        after it."""

        results = []

        # because it is a generator object we can not index it
        for arr in self.data_obj:
            for row in arr:
                if row[0] == part_sp:
                    results.append((row[1], row[2]))
        return results