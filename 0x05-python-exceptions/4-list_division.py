#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, IndexError, TypeError):
            result = 0
            try:
                raise
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
            except TypeError:
                print("wrong type")
        finally:
            results.append(result)
    return results
