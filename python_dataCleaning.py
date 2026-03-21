def calculate_adjusted_revenue(df):
    df['Price'] = df['Price'].fillna(df['Price'].mean())

    filtered = df[df['Returned'] == 'No']

    total_revenue = (filtered['Price'] * filtered['Quantity']).sum()

    return round(total_revenue, 2)
