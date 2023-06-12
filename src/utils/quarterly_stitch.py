import glob
import os
import pandas as pd

csv_files = sorted(glob.glob('data\quarterlyData\*.csv'))
csv_files.reverse()

print(csv_files)

df_list = []

# Loop through each CSV file and add it to the list
for file in csv_files:
    df_list.append(pd.read_csv(file))

# Concatenate all of the dataframes into a single dataframe
final_df = pd.concat(df_list, ignore_index=True)

# Check if there are any duplicated values in the first column of the merged dataframe
duplicated_rows = final_df[final_df.duplicated(subset=final_df.columns[0], keep=False)]

if not duplicated_rows.empty:
    print('WARNING: The following rows have duplicated values in the first column:')
    print(duplicated_rows)

# Sort the final dataframe by the first column
final_df = final_df.sort_values(by=final_df.columns[0])

# Write the final dataframe to a new CSV file
final_df.to_csv('merged.csv', index=False)

print('CSV files successfully stitched together and sorted!')
