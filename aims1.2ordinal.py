import pandas as pd
import numpy as num

dataset={
    "person":["yash","aryan","ayushman","devansh","laksh"],
    "height":["bauna","mid","tall","mid","tall"]
}

df=pd.DataFrame(dataset)
height_position=["bauna","mid","tall"]
mapping ={i:j for j,i in enumerate(height_position)}
print(mapping)
df["height_value"]=df["height"].map(mapping)
print(df)

