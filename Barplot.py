import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

flights_df=sns.load_dataset('flights')


passengers=flights_df['passengers']

sns.barplot(x=flights_df['year'], y=passengers,data=flights_df,estimator=np.median)
plt.show()