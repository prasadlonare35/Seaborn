import seaborn as sns
import matplotlib.pyplot as plt

# Basic Line plot
data = [10, 15, 20, 25, 30, 35, 40]
sns.lineplot(x=[1, 2, 3, 4, 5, 6, 7], y=data)
plt.title("Basic Line Plot")
plt.show()

# built-in dample datasets available in seaborn library
print(sns.get_dataset_names())  # List all available datasets

d1 = sns.load_dataset("titanic").head(20)
sns.lineplot(
    x="age", 
    y="fare", 
    data=d1, 
    hue="sex", 
    style="sex", 
    palette="Accent", 
    markers=["o", ">"], 
    dashes=False
)
plt.title("Titanic Age vs Fare by Gender")
plt.show()