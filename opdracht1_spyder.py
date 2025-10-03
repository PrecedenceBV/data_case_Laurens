import pandas as pd

nps_scores = pd.read_csv('data/nps_scores.csv', delimiter = ';')
call_data = pd.read_csv('data/call_data.csv')
customer_data = pd.read_csv('data/customer_data.csv')
demographics_data = pd.read_csv('data/demographics_data.csv')
order_data = pd.read_csv('data/order_data.csv')
order_line_data = pd.read_csv('data/order_line_data.csv')
product_data = pd.read_csv('data/product_data.csv')

#%%
def calculate_nps(group):
    total = len(group)
    promoters = (group['Recommendation_score'] >= 9).sum()
    detractors = (group['Recommendation_score'] <= 6).sum()
    
    promoter_pct = promoters / total * 100
    detractor_pct = detractors / total * 100
    
    return promoter_pct - detractor_pct

nps_by_journey = nps_scores.groupby('Journey_Type').apply(calculate_nps).reset_index(name='NPS')
#print(nps_by_journey)

#%%
print(call_data.columns.tolist())

#%%
mean_satisfaction = call_data.groupby("Call_Resolved")["Customer_Satisfaction_Score"].mean()


#%%
def correlation_func(group):
    return group['Customer_Satisfaction_Score'].corr(group['Call_Duration_Minutes'])

correlations_by_reason = call_data.groupby('Call_Reason').apply(correlation_func)
print(correlations_by_reason)


#%%
