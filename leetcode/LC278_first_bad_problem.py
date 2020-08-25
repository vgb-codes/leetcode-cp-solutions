def first_bad_problem(n):
    left = 1
    right = n
    while left < right:
        middle = left + int((right-left)/2)
        if isBadVersion(middle):
            right = middle
        else:
            left = middle + 1 
    return left