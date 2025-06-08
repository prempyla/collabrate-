def insertion_sort(seq):
    n=len(seq)
    for i in range(n):
        j=i-1
        k=seq[i]
        while(j>=0 and seq[j]>k):
            seq[j+1]=seq[j]
            j-=1
        seq[j+1]=k
    return seq
