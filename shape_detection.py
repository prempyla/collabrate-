import pandas as pd

def detect_distribution_shape(df: pd.DataFrame) -> str:
    # Calculate skewness of PurchaseAmount
    skewness = df["PurchaseAmount"].skew()
    
    # Determine shape
    if skewness > 0.5:
        return "Right Skewed"
    elif skewness < -0.5:
        return "Left Skewed"
    else:
        return "Symmetric"
