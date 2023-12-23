#apijsonreadcsv.py
import pandas as pd
commute_df = pd.read_csv('commute_data.csv')
print(commute_df.head())
commute_df.columns = ['County and State','Total travel time', 'Total > 90 minutes', 'State Code', 'County Code']
print(commute_df.head())