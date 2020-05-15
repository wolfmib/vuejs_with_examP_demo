


def run(input_list):
    """Pure implementation of ja sort algorithm in Python
    :param input_list:  Some mutable ordered input_list with heterogeneous
    comparable items inside
    :return:  the same input_list ordered by ascending
    >>> run([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> run([])
    []
    >>> run([-2, -5, -45])
    [-45, -5, -2]
    """
    # Marcin Ciura's gap sequence
    gaps = [501, 288, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(input_list):
            temp = input_list[i]
            j = i
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j -= gap
            input_list[j] = temp
            i += 1

    return input_list


if __name__ == "__main__":



    test_list = [-3, -3, -2, 1, 2, 3, 9, 9, 9, 10]

    print(run(test_list))


    