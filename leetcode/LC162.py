def peak_index_mountain_array(search_list):
    if len(search_list) == 3:
        return 1
    
    left = 0
    right = len(search_list) - 1
    
    while left < right:
        middle = left + int((right - left)/2)
        if (search_list[middle] < search_list[middle + 1]):
            left = middle + 1
        else:
            right = middle
    return left
