#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = list()
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
            pass
        except TypeError:
            result = 0
            print("wrong type")
            pass
        except IndexError:
            print("out of range")
            pass
        finally:
            my_list.append(result)
    return my_list
