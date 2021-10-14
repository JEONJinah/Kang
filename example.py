import pandas as pd

print(f"HelloWorld")

data = {
    'Name': ['전진아', '이연우', '김미경', '차혜인'],
    'ID': ['2021-01', '2021-02', '2021-03', '2021-04']
}

df = pd.DataFrame(data)

print(df)