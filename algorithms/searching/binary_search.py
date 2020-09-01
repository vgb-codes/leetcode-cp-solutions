def binary_search(search_list, search_ele):
    n = len(search_list)
    left = 0
    right = n-1
    while left <= right:
        middle = int((left+right)/2)
        if search_list[middle] == search_ele:
            return True
        elif search_list[middle] > search_ele:
            right = middle - 1
        else:
            left = middle + 1
    return False
