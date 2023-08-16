
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

path = str(pathlib.Path("datatr", "raw_data").absolute())
print(path)
print(getAllPathes(path))


