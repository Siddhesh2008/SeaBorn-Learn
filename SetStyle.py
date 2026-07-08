import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

flights_df=sns.load_dataset('flights')


passengers=flights_df['passengers']
sns.set_style('whitegrid')          ##whitegrid, darkgrid, white, dark, ticks
plt.figsize=(10,6)
sns.set_context('notebook', font_scale=1.5, rc={'lines.linewidth':2.5})  ##notebook, talk, poster,paper
sns.despine(left=True, bottom=True)        ##remove the top and right spines
sns.jointplot(x=passengers, y=flights_df['year'], data=flights_df)
plt.show()