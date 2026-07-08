import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

flights_df=sns.load_dataset('flights')


passengers=flights_df['passengers']
sns.countplot(x=passengers,data=flights_df)
plt.tight_layout()
plt.show()