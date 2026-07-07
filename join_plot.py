import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

flights_df=sns.load_dataset('flights')
print(flights_df.head())

passengers=flights_df['passengers']

print(sns.jointplot(x=passengers, y=flights_df['year'], data=flights_df, kind='reg')) #reg,kde,hex      
plt.show()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    