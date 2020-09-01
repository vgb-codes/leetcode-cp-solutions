"""
Bubble Sort
Time Complexity (Average): O(n^2)
Space Complexity (Worst): O(1)
"""


def bubble_sort(sort_list):
    for i in range(len(sort_list)):
        for j in range(len(sort_list) - 1 - i):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list
