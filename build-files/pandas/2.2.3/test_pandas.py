import pandas as pd

# stolen from https://stackoverflow.com/questions/28417293/sample-datasets-in-pandas

file_name = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
df = pd.read_csv(file_name)
print(df.head())