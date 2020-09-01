def binary_search_rec(search_list, search_ele, left, right):
    while left <= right:
        middle = int((left+right)/2)
        if search_list[middle] == search_ele:
            return True
        elif search_list[middle] > search_ele:
            return binary_search_rec(search_list, search_ele, left, middle-1)
        else:
            return binary_search_rec(search_list, search_ele, middle+1, right)
    return False
