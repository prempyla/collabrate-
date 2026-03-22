def calculate_new_york_sales(df):
    
    df['Sales'] = df['Sales'].fillna(0)

    df['City'] = df['City'].str.lower().str.strip()

    total = df[df['City'] == 'new york']['Sales'].sum()
    
    return total
