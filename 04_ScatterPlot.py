import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# simple ScatterPlot
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()

# Modified ScatterPlot
sns.scatterplot(
    x="total_bill", 
    y="tip", 
    data=df, 
    hue="sex",        # Different colors for Male and Female
    style="time",     # Different markers for Lunch and Dinner
    size="size",      # Bubble size based on party size
    palette="coolwarm", 
    sizes=(20, 200),  # Control how small or big bubbles get
    alpha=0.7,        # Make points semi-transparent
    edgecolor="black" # Black borders around points
)

plt.title("Tip vs Total Bill Scatter Plot")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.grid(True)
plt.show()
