
import pandas as pd
train = pd.read_csv("train.csv")

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Simple ratio

simpleRatio = [None]*len(train.description_x)
tokenSortRatio = [None]*len(train.description_x)

for i in range(0,len(train.description_x)):
   simpleRatio[i] = fuzz.ratio(train.description_x[i], train.description_y[i])
   tokenSortRatio[i] = fuzz.token_sort_ratio(train.description_x[i], train.description_y[i])


