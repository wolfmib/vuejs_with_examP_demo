
import copy 



def run(input_list):
    _tem_list = copy.deepcopy(input_list)
    for i in range(len(_tem_list)):
        for j in range(len(_tem_list)-1-i):
            if _tem_list[j] > _tem_list[j+1]:
                _tem_list[j],_tem_list[j+1] = _tem_list[j+1], _tem_list[j]
    
    return _tem_list


if __name__ == "__main__":
    test_list = [27, 33, 4, 28, 2, 26, 13, 35, 8, 14]
    print("[🦉]: C'est bubble_sort")
    print("\n\nOrigin: %s"%test_list)
    print("After : %s"%run(test_list))

    print("---------------------------------\n\n")
    test_list = [27, -33, 4, 28, 2, 26, -13,0, 35, 8, -14]
    print("Origin: %s"%test_list)
    print("After : %s"%run(test_list))