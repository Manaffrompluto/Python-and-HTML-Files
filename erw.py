import seaborn as fdgxzc
import matplotlib.pyplot as dcwejkwe

df = fdgxzc.load_dataset('penguins')
df = df.dropna()

print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print("Species: ", df['species'].unique())
print("Island: ", df['island'].unique())

fdgxzc.histplot(data=df, x='body_mass_g', bins=20, color="steelblue")
dcwejkwe.title("Distribution of Penguin Mass")
dcwejkwe.xlabel("Body Mass")
dcwejkwe.ylabel("Count")
dcwejkwe.show()

fdgxzc.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
dcwejkwe.title("Flipper Length Shape by Species")
dcwejkwe.xlabel("Flipper Length (mm)")
dcwejkwe.ylabel("Count")
dcwejkwe.show()

fdgxzc.histplot(data=df, x='flipper_length_mm', hue='species', color="coral")
dcwejkwe.title("Histogram")
dcwejkwe.xlabel("Flipper Length (mm)")
dcwejkwe.ylabel("Count")
dcwejkwe.show()

fdgxzc.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
dcwejkwe.title("Flipper Length vs Body Mass by Species")
dcwejkwe.xlabel("Flipper Length (mm)")
dcwejkwe.ylabel("Count")
dcwejkwe.show()

c = df.corr(numeric_only=True)
print("Correlation Table")
print(c)
print()
dcwejkwe.figure(figsize=(12, 6))
fdgxzc.heatmap(c, annot=True, cmap='coolwarm')
dcwejkwe.title("Heatmap")
dcwejkwe.show()