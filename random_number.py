"""
Provides a random number of personalizable character length
"""
from time import time


def random_number(length: int)-> int:
    """
    return a random number of character length 'length'
    """
    # getting the current time in int
    cur_time = num_randomizer(time())
    # converting the character length to desired length
    cur_length = len(str(cur_time))
    if length <= cur_length:
        pass
    else:
        while len(str(cur_time)) < length:
            cur_time *= cur_time
    return int(str(cur_time)[:length])


def num_randomizer(num: float) -> int:
    """
    randomizes a number using the current time and
    returns an int value
    """
    num += time()
    num_list = str(num).split('.')
    num_int = int(num_list[1])
    return num_int

# if __name__ == "__main__":
#     print (random_number(1))
