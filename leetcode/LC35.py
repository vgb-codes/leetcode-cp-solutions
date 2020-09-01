def search_insert_index(search_list, x):
    left = 0
    right = len(search_list)
    while left < right:
        middle = left + int((right-left)/2)
        if search_list[middle] >= x:
            right = middle
        else:
            left = middle + 1
    return left
