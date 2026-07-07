import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

flights_df=sns.load_dataset('flights')
print(flights_df.head())

passengers=flights_df['passengers']

sns.kdeplot(flights_df['passengers'])
plt.show()