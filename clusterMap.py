import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy

flights_df=sns.load_dataset('flights')

sns.clustermap(flights_df.pivot_table(index='year',columns='month',values='passengers'),standard_scale=1)  #classifies similar,clusters
plt.show()