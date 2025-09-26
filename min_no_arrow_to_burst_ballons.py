def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])

    count = 1
    element = points[0][1]
    for i in range(1,len(points)):
        if points[i][0] > element:
            count +=1
            element = points[i][1]
    return count
