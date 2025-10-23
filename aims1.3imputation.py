import pandas as pd
import numpy as num
dataset={
    "person":["yash","aryan","ayushman","devansh","laksh","aditya","rohit"],
    "height":[2,3,5,4,5, num.nan, num.nan]
}
df=pd.DataFrame(dataset)
average_height=df["height"].mean()
df["height"].fillna(average_height, inplace=True)
print(df)