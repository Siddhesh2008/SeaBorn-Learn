import seaborn as sns
import matplotlib.pyplot as plt

print(sns.__version__)

flights_df=sns.load_dataset('flights')
print(flights_df.head())

passengers=flights_df['passengers']

print(sns.displot(passengers))
plt.show()