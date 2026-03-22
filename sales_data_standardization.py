
def calculate_new_york_sales(df):
    # Step 1: Fill missing values in 'Sales' with 0
    df['Sales'] = df['Sales'].fillna(0)
    # Step 2: Standardize 'City' strings (lowercase and strip whitespace)
    df['City'] = df['City'].str.lower().str.strip()
    # Step 3: Return the total sum of 'Sales' for 'new york'
    total = df[df['City'] == 'new york']['Sales'].sum()
    return total
