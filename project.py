import pandas as pd
df = pd.read_csv("C:\\Users\\priya\\AppData\\Local\\Programs\\Python\\Python312\\NewCompanyDetails.csv")
df = df.drop_duplicates()
df = df.dropna()
df['revenue'] = df['revenue'].replace('[^0-9]', '', regex=True).astype(int)
df['Total Workers'] = df['workers'] + df['previous_workers']
df.to_csv("NewCompanyDetails2.csv", index=False)
print('completed')
