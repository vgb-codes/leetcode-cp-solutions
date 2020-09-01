"""
Insertion Sort
Time Complexity (Average): O(n^2)
Space Complexity (Worst): O(1)
"""


def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j = j - 1
        sort_list[j + 1] = key
    return sort_list
