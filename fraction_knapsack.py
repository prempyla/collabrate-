def fractionalKnapsack(val, wt, capacity):
    n=len(val)
    valByWtArr = []
    value = 0.0

    for i in range(n):
        val_by_wt = val[i]/wt[i]
        valByWtArr.append((val_by_wt,i))
    valByWtArr.sort(reverse=True)

    for pair in valByWtArr:
        valByWt = pair[0]
        idx = pair[1]

        if capacity >= wt[idx]:
            capacity = capacity - wt[idx]
            value = val[idx]+ value
        else:
            value = value + (capacity*valByWt)
            break

    return format(value, ".6f")
