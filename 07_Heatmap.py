import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

numeric_df = df.select_dtypes(include=["number"])        # Select only numeric columns
corr = numeric_df.corr()        # Compute correlation matrix

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Numerical Features Only)")
plt.show()

