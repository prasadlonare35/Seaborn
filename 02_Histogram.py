import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.histplot(df["total_bill"], bins=10, kde=True)
plt.show()

sns.displot(df["total_bill"], bins=10, kde=True,rug=True,color="r")
plt.show()
