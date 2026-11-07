import seaborn as dasea
import matplotlib.pyplot as matplottingorsomething

df = dasea.load_dataset('tips')
df = df.dropna()

print(df.head())
print(df.info())

dasea.barplot(data=df, x='day', y='total_bill', hue='sex', color="coral")
matplottingorsomething.title("Average Total Bill per Day (by Gender)")
matplottingorsomething.xlabel("Day")
matplottingorsomething.ylabel("Average Bill ($)")
matplottingorsomething.show()

dasea.countplot(data=df, x='day', hue='sex', color="green")
matplottingorsomething.title("Number of Diners per Day (by Gender)")
matplottingorsomething.xlabel("Day")
matplottingorsomething.ylabel("Count")
matplottingorsomething.show()

dasea.boxplot(data=df, x='day', y='total_bill', color="orange")
matplottingorsomething.title("Total Bill per Day")
matplottingorsomething.xlabel("Day")
matplottingorsomething.ylabel("Total Bill ($)")
matplottingorsomething.show()

dasea.stripplot(data=df, x='day', y='total_bill', color="red", jitter=True)
matplottingorsomething.title("Bill Amount per Day (Strip Plot)")
matplottingorsomething.xlabel("Day")
matplottingorsomething.ylabel("Total Bill ($)")
matplottingorsomething.show()

dasea.swarmplot(data=df, x='day', y='total_bill', color="purple")
matplottingorsomething.title("Bill Amount per Day (Swarm Plot)")
matplottingorsomething.xlabel("Day")
matplottingorsomething.ylabel("Total Bill ($)")
matplottingorsomething.show()

dasea.jointplot(data=df, x='total_bill', y='tip', color="steelblue")
matplottingorsomething.suptitle("Total Bill vs Tip")
matplottingorsomething.show()

dasea.jointplot(data=df, x='total_bill', y='tip', color="yellow")
matplottingorsomething.suptitle("Total Bill vs Tip (Joint Plot)")
matplottingorsomething.show()

dasea.pairplot(df[['total_bill', 'tip', 'size']])
matplottingorsomething.suptitle("Bill, Tip and Size")
matplottingorsomething.show()

dasea.pointplot(data=df, x='day', y='total_bill', hue='sex', color="cyan")
matplottingorsomething.title("Average Total Bill per Day (by Gender)")
matplottingorsomething.xlabel("Day")
matplottingorsomething.ylabel("Average Bill ($)")
matplottingorsomething.show()

dasea.lmplot(data=df, x='total_bill', y='tip')
matplottingorsomething.title("Total Bill vs Tip - from Temu")
matplottingorsomething.show()