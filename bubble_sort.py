def bubble_sort(mylist):
    n = len(mylist)
    copy_list = mylist.copy()

    for i in range(n-1):
        for j in range(n-i-1):
            if copy_list[j] > copy_list[j+1]:
                copy_list[j], copy_list[j+1] = copy_list[j+1], copy_list[j]
                break
    
    return copy_list