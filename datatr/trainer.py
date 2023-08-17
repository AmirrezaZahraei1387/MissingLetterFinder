# standard library
import os
import csv


# third party libraries
from nltk.tokenize import word_tokenize
from nltk import bigrams, pos_tag


class Counter:

    CountedElements = {}

    def addElement(self, array):

        for element in array:

            if element in self.CountedElements:
                self.CountedElements[element] += 1

            else:
                self.CountedElements.update({element: 1})

    def __add__(self, items):
        self.addElement(items)
        return self


def getAllPathes(folder: str):
    all_file_names = os.listdir(folder)

    pathes = []

    for name in all_file_names:
        pathes.append(os.path.join(folder, name))

    return pathes


class TrainMC:

    def __init__(self, raw_data_folder: str):

        self.raw_data_folder = raw_data_folder

        self.all_raw_data_files = getAllPathes(self.raw_data_folder)

    def train(self):

        counter = Counter()

        for path in self.all_raw_data_files:
            print(path)
            with open(path, mode="r") as file:
                lines = file.readlines()

                for line in lines:

                    tokens = word_tokenize(line)
                    tagged_tokens = pos_tag(tokens)

                    # the output of the tagged tokens is a zipped tuple of the word and its tag. we do not want
                    # the part of the word
                    if tagged_tokens:

                        tags = list(zip(*tagged_tokens))[1]
                        tags = bigrams(tags)

                        counter += tags

        return counter


def writeCsv(re_data_folder: str, re_data_name: str, counter: Counter):

    new_path = os.path.join(re_data_folder, re_data_name)

    with open(new_path, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for item in counter.CountedElements.items():
            print(item)
            writer.writerow([item[0][0], item[0][1],  item[1]])
