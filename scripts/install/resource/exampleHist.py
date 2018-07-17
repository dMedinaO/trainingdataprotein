import seaborn as sns
df = sns.load_dataset('iris')

# Method 1: on the same Axis
print df["sepal_width"]
sns.distplot( df["sepal_width"] , color="red", label="Sepal Width")
sns.plt.legend()

sns.plt.show()
