def calculate_adjusted_revenue(df):
    # Step 1: Fill missing Price values with the mean of the 'Price' column
    df['Price'] = df['Price'].fillna(df['Price'].mean())
    # Step 2: Filter the DataFrame to keep only rows where Returned is 'No'
    filtered = df[df['Returned'] == 'No']
    # Step 3: Calculate total revenue (Price * Quantity) for the remaining rows
    total_revenue = (filtered['Price'] * filtered['Quantity']).sum()
    # Step 4: Return the total revenue as a float, rounded to 2 decimal places
    return round(total_revenue, 2)
