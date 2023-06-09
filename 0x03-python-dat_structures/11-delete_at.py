#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete an element in a list
    
    Args:
        my_list: The list
        idx: Index to delete at
    
    Returns:
        A modified list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
