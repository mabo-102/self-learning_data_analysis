import pandas as pd

# データフレームの作成
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Kelly', 'Leo', 'Mia', 'Nina', 'Oliver'],
        'Age': [25, 30, 35, 28, 40, 32, 37, 29, 31, 33, 36, 27, 38, 26, 39],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# データフレームの基本的な操作
print("First few rows of the DataFrame:")
print(df.head())

print("\nInformation about the DataFrame:")
print(df.info())

print("\nStatistical summary of the DataFrame:")
print(df.describe())

# データの選択とフィルタリング
selected_column = df['Age']
print("\nSelected column 'Age':")
print(selected_column)

filtered_data = df[df['Age'] > 30]
print("\nData where Age is greater than 30:")
print(filtered_data)

# データの変更と追加
df.loc[1, 'Age'] = 31
df['Salary'] = [50000, 60000, 70000, 55000, 62000, 75000, 68000, 85000, 60000, 70000, 78000, 59000, 54000, 72000, 76000]

print("\nDataFrame after modifications:")
print(df)

# データのグループ化と集計
numeric_columns = df.select_dtypes(include='number')
grouped_data = numeric_columns.groupby(df['City']).mean()
print("\nGrouped data with average Age and Salary:")
print(grouped_data)