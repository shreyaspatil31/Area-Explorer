import numpy as np
import pandas as pd

# Reading excel sheet
df = pd.read_excel("C:\\Users\\shrey\\Documents\\CODE\\CODE\\assets\\xlsx\\dataset.xlsx")

# Creating virtual table(s)
df['x2'] = df['y2'] = df['ah'] = df['aw'] = df['area'] = np.nan

# Doing mathematical operations and storing values to recently created tables
for i in range(len(df['x1'])):
    if (i != len(df['x1'])-1):
        df.loc[i, 'x2'] = df.loc[i+1, 'x1']
        df.loc[i, 'y2'] = df.loc[i+1, 'y1']
    else:
        df.loc[i, 'x2'] = df.loc[0, 'x1']
        df.loc[i, 'y2'] = df.loc[0, 'y1']

    df.loc[i, 'ah'] = (df.loc[i, 'y2'] + df.loc[i, 'y1']) / 2
    df.loc[i, 'aw'] = df.loc[i, 'x2'] - df.loc[i, 'x1']

    df.loc[i, 'area'] = df.loc[i, 'ah'] * df.loc[i, 'aw']

# Calculating area in pixel as well as in cm2
pxArea = 0
for i in range(len(df['area'])):
    pxArea += df['area'][i]

cmArea = pxArea/(1080)

print(df)
print(f'\nTotal area in pixel: {pxArea}')
print(f'Total  area in cm2: {cmArea}')


#For simpsons 1/3 rule
# df['x3'] = np.nan
# for i in range(len(df['x1'])):
#     if(df['x1']==df['x1']+1):
#         df['x3']=df['y1']-(df['y1']+1)
        
# print(df['x3'])

print(" ")

# Find the difference in 'y2' when 'x1' is the same for any two rows in the dataset
df['x2_difference'] = np.nan
# Finding difference of 'y2' when 'x2' is the same for any two rows
for i in range(len(df['y2'])):
    for j in range(i+1, len(df['y2'])):
        if df['y2'][i] == df['y2'][j]:
            df.loc[j, 'x2_difference'] = abs(df['x2'][j] - df['x2'][i])

non_nan_count = df['x2_difference'].count()
print(f'Count of non-NaN values in x2_difference: {non_nan_count}')

print(df)

# Filter non-NaN values of 'y2_difference'
non_nan_values = df.loc[~df['x2_difference'].isna(), ['x2_difference']]

# Save non-NaN values in a new Excel sheet
non_nan_values.to_excel("C:\\Users\\shrey\\Documents\\CODE\\CODE\\assets\\xlsx\\y2_difference_sheet.xlsx", index=False)