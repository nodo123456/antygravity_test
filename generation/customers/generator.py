import pandas as pd
import random

def generate():
    print("Generating customer data...")
    
    user_ids = range(1001, 1101) # 100 users matching events
    names = [f"User_{i}" for i in user_ids]
    countries = ['US', 'UK', 'CA', 'DE', 'FR', 'JP', 'AU']
    
    data = {
        'user_id': user_ids,
        'name': names,
        'email': [f"user{i}@example.com" for i in user_ids],
        'country': [random.choice(countries) for _ in user_ids]
    }
    
    df = pd.DataFrame(data)
    return df
