#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specified position
    without modifying the original list
    args:
        my_list - The list
        idx - index to replace
        element - new element to be inserted
    """
    if idx < 0 or idx >= len(my_list):
        return list(my_list)
    l2 = list(my_list)
    l2[idx] = element
    return l2
