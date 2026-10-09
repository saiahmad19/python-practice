import pandas as pd

data = {
    "name": ["pen", "notebook", "bag"],
    "price": [2, 5, 40],
    "in_stock": [100 , 30, 5]
}

df = pd.DataFrame(data)
df["low_stock"] = df["in_stock"] < 10
low_stoc = df[df["low_stock"]]
print(df)
print(df["price"])
print(low_stoc)
