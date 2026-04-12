def most_common_complaint(df):
    counts = df['ComplaintType'].value_counts()

    max_count = counts.max()
    
    top_complaints = counts[counts == max_count].index.tolist()
    
    for complaint in df['ComplaintType']:
        if complaint in top_complaints:
            return complaint
