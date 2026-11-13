import numpy as n
import pandas as p
import seaborn as s
import matplotlib.pyplot as m

print(s.get_dataset_names())
df = s.load_dataset('penguins')

print(df.head(10))
print(df.shape)
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df.describe(include='all'))
print(df.corr(numeric_only=True))

s.heatmap(df.corr(numeric_only=True), annot=True)
m.show()

df.select_dtypes(include=[n.number]).plot(kind='box', subplots=True, layout=(3, 2), sharex=False, sharey=False, figsize=(8, 12))
m.show()

print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())

s.countplot(data=df, x='sex', color="yellow")
m.show()
s.countplot(data=df, x='island', color="lightblue")
m.show()
s.countplot(data=df, x='species', color="green")
m.show()

s.countplot(data=df, x='sex', hue='species', color="coral")
m.show()
s.countplot(data=df, x='island', hue='species', color="olive")
m.show()
s.countplot(data=df, x='island', hue='sex', color="darkslategray")
m.show()

s.pairplot(data=df, hue='species')
m.show()