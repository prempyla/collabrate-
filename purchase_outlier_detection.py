def calculate_outlier_proportion(df):
    Q1 = df['PurchaseAmount'].quantile(0.25)
    Q3 = df['PurchaseAmount'].quantile(0.75)
    
    IQR = Q3 - Q1
    
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[df['PurchaseAmount'] > upper_bound]
    
    result = len(outliers) / len(df)
    
    return round(result, 2)
