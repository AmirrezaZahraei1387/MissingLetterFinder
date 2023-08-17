
# standard library
import os
import csv
import pathlib

# third party libraries
from nltk.tokenize import word_tokenize
from nltk import bigrams, pos_tag
from numpy import array
from numpy import unique


def getAllPathes(folder: str):

    all_file_names = os.listdir(folder)

    pathes = []

    for name in all_file_names:
        pathes.append(os.path.join(folder, name))

    return pathes



PATH_RAW_DATA_D = str(pathlib.Path("datatr", "raw-data").absolute())
PATH_RE_DATA_D = str(pathlib.Path("datatr", "re-data").absolute())

NAME_DATA_F = "data_fs_d.csv"
PATH_RAW_DATA_FILES_F = getAllPathes(PATH_RAW_DATA_D)




for path in PATH_RAW_DATA_FILES_F:

    with open(path, encoding="utf-8", mode="r") as file:
        texture = file.read()

        tokens = word_tokenize(texture)
        tagged_tokens = pos_tag(tokens)

        # the output of the tagged tokens is a zipped tuple of the word and its tag. we do not want
        # the part of the word
        tags = array(list(zip(*tagged_tokens))[1])

        element, count = unique(tags, return_counts= True)

        count_elements = dict(zip(element, count))