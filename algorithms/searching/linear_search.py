def linear_search(search_list, search_ele):
    # Computing number of elements in search list
    n = len(search_list)
    # Looping through list to find element
    for i in range(n):
        if (search_list[i] == search_ele):
            return True
    return False
