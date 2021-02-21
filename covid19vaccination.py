import pandas as pd
import numpy as np
pd.options.display.max_columns = 50

dataset = pd.read_csv(r'C:\Users\MSI RadTek\OneDrive - Institut Teknologi Sepuluh Nopember\Data Science\DataSets\country_vaccinations.csv')
print('Take a brief look into the data',dataset.head())
print('\n descrribe dataset',dataset.describe())
print('\nsize:',dataset.shape)

# HANDLING MISSING VALUES
tot_nan = dataset.isna().sum().sum()
tot_cell = np.product(dataset.shape)
percentage_nan = tot_nan/tot_cell*100
print('\nNaN Percentage :',percentage_nan)

print('\nnan values :')
print(dataset.isna().sum().sort_values(ascending=False))

print(dataset.shape)
dataset.dropna(subset=['people_vaccinated','total_vaccinations'],inplace=True)
print(dataset.shape)

dataset['people_fully_vaccinated'].fillna(dataset['total_vaccinations'] - dataset['people_vaccinated'], inplace=True)

dataset = dataset.reset_index(drop=True)
for i in range(1,dataset.shape[0]-1):
    dataset.loc[i,'daily_vaccinations_raw'] = dataset.loc[i,'total_vaccinations'] - dataset.loc[i-1,'total_vaccinations']
dataset = dataset[dataset['daily_vaccinations_raw'] > 0]

dataset.drop(['people_fully_vaccinated_per_hundred'], axis=1,inplace=True)

iso_code = list(dataset['country'][dataset['iso_code'].isna()].drop_duplicates())
print("\nCountry that has ISO Code missing values are :")
print(iso_code)
dataset = dataset.reset_index(drop=True)
for i in range(dataset.shape[0]):
    if dataset.loc[i,'country'] == 'England':
        dataset.loc[i,'iso_code'] = "GB-ENG"
    elif dataset.loc[i,'country'] == 'Northern Ireland':
        dataset.loc[i, 'iso_code'] = "GB"
    elif dataset.loc[i,'country'] == 'Scotland':
        dataset.loc[i, 'iso_code'] = "GB-SCT"
    elif dataset.loc[i,'country'] == 'Wales':
        dataset.loc[i, 'iso_code'] = "Unknown"

dataset.dropna(inplace=True)
print(dataset.isna().sum().sort_values(ascending=False))
