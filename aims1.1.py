import pandas as pd
import numpy as num

dataset={
    "person":["yash","aryan","ayushman","devansh","laksh"],
    "height":["bauna","mid","tall","mid","tall"]
}

df=pd.DataFrame(dataset)
heightranges=df["height"].unique()
for i in heightranges:
    height_range="height_" + str(i)
    df[height_range]=(df["height"]==i).astype(int)

print(df)