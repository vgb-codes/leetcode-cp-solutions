import sys

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

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid Arguments!")
    else:
        search = [int(i) for i in sys.argv[1].split(',')]
        element = int(sys.argv[2])
        print(binary_search_rec(search, element, 0, len(search)-1))
