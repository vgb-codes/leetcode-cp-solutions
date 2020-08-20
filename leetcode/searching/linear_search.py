import sys

def linear_search(search_list, search_ele):
    #Computing number of elements in search list
    n = len(search_list)
    #Looping through list to find element
    for i in range(n):
        if (search_list[i]==search_ele):
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid Arguments!")
    else:
        search = [int(i) for i in sys.argv[1].split(',')]
        element = int(sys.argv[2])
        print(linear_search(search, element))
