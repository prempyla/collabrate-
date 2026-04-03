import pandas as pd

def calculate_distribution(sales_df):
    df = sales_df.dropna(subset=["Category"])
    
    freq = df["Category"].value_counts()
    total = freq.sum()
    
    rel_freq = (freq / total).round(2)
    
    result = pd.DataFrame({
        "Category": freq.index,
        "Frequency": freq.values,
        "Relative_Frequency": rel_freq.values
    })
    
    result = result.sort_values(
        by=["Frequency", "Category"],
        ascending=[False, True]
    )
    
    output = result.values.tolist()
    
    return output
