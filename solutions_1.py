import pandas as pd
# Assuming file name is test.csv
dataFrame = pd.read_csv("test.csv")
dataFrame.sort_index(axis=1).to_csv("output_csv.csv",index=False)