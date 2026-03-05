def bubble_sort(mylist):
    """Generator-based bubble sort that yields the list state and swap indices
    after each swap, enabling smooth step-by-step animation."""
    n = len(mylist)
    copy_list = mylist.copy()

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if copy_list[j] > copy_list[j + 1]:
                copy_list[j], copy_list[j + 1] = copy_list[j + 1], copy_list[j]
                swapped = True
                yield copy_list, j, j + 1
        if not swapped:
            break