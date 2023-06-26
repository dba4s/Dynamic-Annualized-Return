import pandas as pd
import numpy as np

def calculate_annualized_geometric_return(df):
    
    # Initialize an empty array to store the annualized returns
    annualized_returns = np.empty(len(df.columns) - 1)
    
    for i, column in enumerate(df.columns[1:]):
        # Find the first non-missing return for the current fund
        start_date = df[column].first_valid_index()
        
        # Find the last non-missing return for the current fund
        end_date = df[column].last_valid_index()
        
        # Calculate the time period in number of periods
        time_periods = (end_date - start_date)

        # Find the non-missing returns for the current fund
        returns = df[column].replace('---', np.nan).astype(float) 
        
        # Calculate the product of (1 + return)
        returns_plus_one = returns + 1 # add 1 to each return in returns 
        product = returns_plus_one.prod()
        
        # Calculate the annualized geometric return for the current fund
        annualized_return = (product ** (12 / time_periods)) - 1
        
        # Store the annualized return in the result array
        annualized_returns[i] = annualized_return
    
    return annualized_returns

# Read Excel file
df = pd.read_excel('returns.xlsx')

print(calculate_annualized_geometric_return(df))

