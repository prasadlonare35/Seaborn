import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# simple BoxPlot
sns.boxplot(x="day", y="total_bill", data=df,showmeans=True)
plt.title("Simple BoxPlot")
plt.show()

# Modified BoxPlot
sns.boxplot(
    x="day", 
    y="total_bill", 
    data=df, 
    hue="sex",           # Adds split by Male/Female
    showmeans=True,      # Shows the mean as a dot
    meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black"},
    palette="Set2",      # Adds a pastel color palette
    linewidth=2,         # Thicker box lines
    width=0.6            # Controls box width
)

plt.title("BoxPlot of Total Bill by Day and Gender")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.grid(True, linestyle="--", alpha=0.5) 
plt.legend(title="Gender")
plt.show()
