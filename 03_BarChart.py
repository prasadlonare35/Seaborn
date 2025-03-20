import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=df, hue="sex", ci=20)
plt.title("Average Total Bill per Day (by Gender)")
plt.show()
