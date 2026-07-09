import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
#crashed=sns.load_dataset('car_crashes')

#sns.heatmap(crashed.select_dtypes(include=['number']).corr(),cmap='Blues',annot=True)
#plt.show()

flights_df=sns.load_dataset('flights')

sns.heatmap(flights_df.pivot_table(index='year',columns='month',values='passengers'),cmap='Blues')
plt.show()