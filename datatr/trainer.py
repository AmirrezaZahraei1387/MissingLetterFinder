# standard library
import os
import csv
import collections
import pathlib

# third party libraries
from nltk.tokenize import word_tokenize
from nltk import bigrams, pos_tag


def getAllPathes(folder: str):
    all_file_names = os.listdir(folder)

    pathes = []

    for name in all_file_names:
        pathes.append(os.path.join(folder, name))

    return pathes


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




# PATH_RAW_DATA_D = str(pathlib.Path("raw-data").absolute())
# PATH_RE_DATA_D = str(pathlib.Path("re-data").absolute())
#
# NAME_DATA_F = "data_fs_d.csv"
# PATH_RAW_DATA_FILES_F = getAllPathes(PATH_RAW_DATA_D)
#
# all_tags = array([(9, 8), (0, 8)])
# counted_tag = {}
#
#
# for path in PATH_RAW_DATA_FILES_F:
#
#     with open(path, encoding="utf-8", mode="r") as file:
#         texture = file.read()
#
#         tokens = word_tokenize(texture)
#         tagged_tokens = pos_tag(tokens)
#
#         # # the output of the tagged tokens is a zipped tuple of the word and its tag. we do not want
#         # # the part of the word
#         # tags = array(list(zip(*tagged_tokens))[1])
#         # tags = list(bigrams(tags))
#         #
#         # all_tags = concatenate((all_tags, tags))
#
#     counted_tag = collections.Counter(tags)
#
# print(counted_tag)
#
#
# a = array([(5, 7), (7, 6)])
# counter = collections.Counter(a)
#
# print(counter)
