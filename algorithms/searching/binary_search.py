import sys

def binary_search(search_list, search_ele):
    #Computing number of elements
    n = len(search_list)
    left = 0
    right = n-1
    #Dividing step
    while left<=right:
        middle = int((left+right)/2)
        if search_list[middle] == search_ele:
            return True
        elif search_list[middle] > search_ele:
            right = middle - 1
        else:
            left = middle + 1
    return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid Arguments!")
    else:
        search = [int(i) for i in sys.argv[1].split(',')]
        element = int(sys.argv[2])
        print(binary_search(search, element))
