def guess_number(n):
    if n <=1:
        return n
    left = 1
    right = n 
    while (left < right):
        middle = left + int((right-left)/2)
        if guess(middle) == 0:
            return middle
        elif guess(middle) == -1:
            right = middle
        else:
            left = middle + 1
    return left
