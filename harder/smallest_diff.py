def smallest_diff(a, b):
    """Return smallest diff between all items in a and b.

        >>> smallest_diff([10, 20, 30, 40], [15, 25, 33, 45])
        3

        [10, 20, 22*, 25*, 30, 33*, 40, 45*]
    """
    a.sort()
    b.sort()

    smallest_diff = float('inf') 
    ia = ib = 0

    while ia < len(a) and ib < len(b):
        curr_diff = abs(a[ia]-b[ib])

        if curr_diff == 0:
            return 0
        
        smallest_diff = min(smallest_diff, curr_diff)

        if a[ia] > b[ib]:
            ib+=1
        else:
            ia+=1

    return smallest_diff



a = [10, 20, 14, 16, 18]
b = [30, 23, 54, 33, 96]

print smallest_diff(a,b)