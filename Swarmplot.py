import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

flights_df=sns.load_dataset('tips')


passengers=flights_df['day']
year=flights_df['total_bill']
sex=flights_df['sex']
sns.violinplot(x=passengers,y=year,data=flights_df,hue=sex,split=True)
sns.swarmplot(x=passengers,y=year,data=flights_df,hue=sex)
plt.show()