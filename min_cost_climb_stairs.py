def min_cost_to_climb(cost):
    return f(0, cost)

def f(ind, cost):
    if ind == len(cost)-1:
        return 0

    oneJump=0
    twoJump=0

    if ind < len(cost):
        oneJump = abs(cost[ind]) + f(ind+1, cost)
    if ind+1 < len(cost):
        twoJump = abs(cost[ind+1]) + f(ind+2, cost)

    return min(oneJump,twoJump)
