def sqrt(x):
    if (x < 2):
        return x
    left = 1
    right = x

    while left < right:
        middle = left + int((right-left)/2)
        if (middle*middle > x):
            right = middle
        else:
            left = middle + 1
    return left - 1
