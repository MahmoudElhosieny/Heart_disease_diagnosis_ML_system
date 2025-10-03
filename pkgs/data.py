import pandas as pd




clean_data = pd.read_csv(r'data\clean_data.csv')
row_data = pd.read_csv(r'data\heart_disease.csv')

clean_data['new_target'] = clean_data['num'].apply(lambda x: 1 if x > 0 else 0)
print('done')