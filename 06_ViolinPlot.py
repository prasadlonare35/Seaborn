import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# simple
sns.violinplot(x="day", y="total_bill", data=df)
plt.show()


# modified
sns.violinplot(
    x="day", 
    y="total_bill", 
    data=df, 
    hue="sex",               # Split by Male/Female inside each violin
    split=True,              # Splits violins by hue categories
    inner="quartile",        # Shows median & quartiles inside the violin
    palette="Pastel1",       # Use a soft pastel color palette
    linewidth=1.5,           # Thicker border line
    bw=0.9                   # Adjusts smoothing (bandwidth)
)

plt.title("Violin Plot of Total Bill by Day and Gender")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend(title="Gender")
plt.show()
