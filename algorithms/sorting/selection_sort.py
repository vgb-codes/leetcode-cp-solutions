def selection_sort(sort_list):
    for i in range(len(sort_list)):
        min_ele = i
        for j in range(i + 1, len(sort_list)):
            if sort_list[j] < sort_list[min_ele]:
                min_ele = j
        sort_list[i], sort_list[min_ele] = sort_list[min_ele], sort_list[i]
    return sort_list
