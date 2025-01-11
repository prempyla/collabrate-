
def sorted_list(list_of_integers):
    n = len(list_of_integers)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_of_integers[j] < list_of_integers[j+1]:  
                list_of_integers[j], list_of_integers[j+1] = list_of_integers[j+1], list_of_integers[j]
    
    return list_of_integers
