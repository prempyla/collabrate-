def count_salary_outliers(df):
    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
    
    return len(outliers)
