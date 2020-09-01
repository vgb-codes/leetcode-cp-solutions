"""
Merge Sort
Time Complexity (Average): O(n*log(n))
Space Complexity (Worst): O(n)
"""


def merge_sort(sort_list, left, right):
    if (left < right):
        middle = left + int((right-left)/2)
        merge_sort(sort_list, left, middle)
        merge_sort(sort_list, middle + 1, right)
        merge(sort_list, left, middle, right)


def merge(sort_list, left, middle, right):
    ele_a = middle - left + 1
    ele_b = right - middle
    list_a = [0]*ele_a
    list_b = [0]*ele_b

    for i in range(ele_a):
        list_a[i] = sort_list[left + i]

    for j in range(ele_b):
        list_b[j] = sort_list[middle + 1 + j]

    a = b = 0
    c = left

    while ((a < ele_a) and (b < ele_b)):
        if (list_a[a] <= list_b[b]):
            sort_list[c] = list_a[a]
            a = a + 1
        else:
            sort_list[c] = list_b[b]
            b = b + 1
        c = c + 1

    while (a < ele_a):
        sort_list[c] = list_a[a]
        a = a + 1
        c = c + 1

    while (b < ele_b):
        sort_list[c] = list_b[b]
        b = b + 1
        c = c + 1
