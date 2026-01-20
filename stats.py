import pandas as pd

data = {
    "player": ["Judge", "Ohtani", "Trout"],
    "hits": [2, 3, 1],
    "at_bats": [4, 5, 3]
}

df = pd.DataFrame(data)
df["average"] = df["hits"] / df["at_bats"]

print(df)