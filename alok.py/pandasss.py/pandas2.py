import pandas as pd 

data={
    'sub':["Math", "Science", "English"],
    'marks':[90, 85, 78]
}

df = pd.DataFrame(data)
print(df)
print(pd.__version__)