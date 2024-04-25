def run(input_list, val):

  
    fib_N_2 = 0
    fib_N_1 = 1
    fibNext = fib_N_1 + fib_N_2
    length = len(input_list)
    if length == 0:
        return 0
    while fibNext < len(input_list):
        fib_N_2 = fib_N_1
        fib_N_1 = fibNext
        fibNext = fib_N_1 + fib_N_2
    index = -1
    while fibNext > 1:
        i = min(index + fib_N_2, (length - 1))
        if input_list[i] < val:
            fibNext = fib_N_1
            fib_N_1 = fib_N_2
            fib_N_2 = fibNext - fib_N_1
            index = i
        elif input_list[i] > val:
            fibNext = fib_N_2
            fib_N_1 = fib_N_1 - fib_N_2
            fib_N_2 = fibNext - fib_N_1
        else:
            return i
    if (fib_N_1 and index < length - 1) and (input_list[index + 1] == val):
        return index + 1
    return -1


if __name__ == "__main__":
    test_list = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130]
    print("[Jean]:  test_list est     =",test_list)
    search_key = int(input("[Jean]:  Entrer la seach number SVP ,    20, 33 etc..\n"))
    _index = run(test_list,search_key)
    print("----------------------------\n")
    print("Result est index    [%d]   , value = %4d             "%(_index,test_list[_index]))
    



