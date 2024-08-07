#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list1[i] / my_list2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
