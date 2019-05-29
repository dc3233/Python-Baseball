import pandas as pd
import matplotlib.pyplot as plt

from data import games # import var games from data script

attendance = games.loc[(games['type'] == 'info') # make new dataframe based on conditions and specific columns
    & (games['multi2'] == 'attendance'), 
    ['year', 'multi3']]

attendance.columns = ['year', 'attendance'] # assign column names to new attendance dataframe

attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance']) # make all rows in attendance col numeric and replace
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')

plt.show()