import pandas as pd

customer_data = pd.read_csv('data/customer_data.csv')

#%%
nan_df = customer_data[customer_data.isna().any(axis=1)]


customer_data = customer_data[customer_data['Age'] >= 12]
#%%
max_age = customer_data['Age'].max()
print(f"Maximum age: {max_age}")
