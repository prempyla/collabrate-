def findTheWinner(n, k):
    friends = list(range(1, n + 1))
    index = 0
    
    while len(friends) > 1:
        index = (index + k - 1) % len(friends)
        friends.pop(index)
    
    return friends[0]
