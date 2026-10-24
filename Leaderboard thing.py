import pandas as pd

s = (98900, 98700, 98600, 98500, 98300)
p = pd.Series(s, index=["Timmy", "Dum", "chng kHiNg", "gayB0i", "iliketogoon"])
print(p)
print()

d = {'Players': ["Timmy", "Dum", "chng kHiNg", "gayB0i", "iliketogoon"], 'Level': [100, 100, 99, 95, 94],'Score': [98900, 98700, 98600, 98500, 98300], 'Wins': [9890, 9870, 9860, 9850, 9830]}
df = pd.DataFrame(d)
print(df)
print()

print("Top player: ")
print(df.loc[0])
print()
print("Second and third top players: ")
print(df.loc[2:3])
print()

fdf = pd.read_csv('ldb.csv')
print("First 5 rows: ")
print(fdf.head())
print("Last 3 rows: ")
print(fdf.tail(3))