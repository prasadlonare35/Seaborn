import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# simple
sns.pairplot(df)
plt.suptitle("Simple Pairplot")
plt.show()

# modified
sns.pairplot(
    df,
    hue="sex",               # Color points by gender
    palette="Set2",          # Softer color palette
    diag_kind="kde",         # Use KDE plots on the diagonal
    markers=["o", "s"],      # Different markers for male and female
    corner=True,             # Show only lower triangle to reduce clutter
    plot_kws={"alpha": 0.6, "s": 60}  # Transparency and point size
)
plt.suptitle("Pairplot of Tips Dataset (Colored by Gender)")
plt.show()
