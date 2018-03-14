import pandas as pd
import string
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import csv
import itertools
import pickle
import firstDialog

firstDialog.Dialog()

import findingIntents

findingIntents.findIntent()

import python_dependency

df = python_dependency.pythondependency()
