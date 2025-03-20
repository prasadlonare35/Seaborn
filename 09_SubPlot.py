import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(x="day", y="total_bill", data=df, ax=axes[0])  # First plot
sns.histplot(df["total_bill"], bins=10, kde=True, ax=axes[1])  # Second plot

plt.show()
