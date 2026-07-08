import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

flights_df=sns.load_dataset('tips')

sns.stripplot(x='day',y='total_bill',data=flights_df,jitter=True,hue='sex',dodge=True)
plt.legend(loc=0)
plt.show()