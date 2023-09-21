#import packages
import matplotlib.pyplot as plt

# define summary statistics function
def sum_stats(data):
    return data.describe()

# define visualization function
def hist(data):
    plt.hist(data["calories"], bins=10, color="purple")
    plt.xlabel("Calories")
    plt.ylabel("Frequency")
    plt.title("Cereal Calories Histogram")
    plt.show()
    plt.savefig("Cereal Calories.png")
    return

def scatterplot(data):
    plt.scatter(data["sugars"],data['calories'],alpha=0.5)
    plt.xlabel("Sugar")
    plt.ylabel("Calories")
    plt.title("Cereal Sugar vs. Calories")
    plt.show()
    plt.savefig("Cereal Scatter.png")
    return
