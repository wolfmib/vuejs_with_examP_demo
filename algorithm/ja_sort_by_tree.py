"""

sort_list by Tree


"""


class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def adjointer(self,val):
        if val < self.val:
            if self.left:
                self.left.adjointer(val)
            else:
                self.left = node(val)
            
        elif val >= self.val:
            if self.right:
                self.right.adjointer(val)
            else:
                self.right = node(val)

def _sort(node,return_list):

    if node:
        _sort(node.left,return_list)
        return_list.append(node.val)
        _sort(node.right,return_list)
    


def run(input_list):
    if len(input_list) == 0:
        return input_list
    
    # Initial
    _node = node(input_list[0])

    # Add _node
    for index in range(1,len(input_list)):
        _node.adjointer(input_list[index])
    
    # Obtenir les resutat
    sorted_list = []
    _sort(_node,sorted_list)
    return sorted_list


if __name__ == "__main__":

    print(run([10, 1, 3, 2, 9, 14, 13]))


    print(run([10, 1, 3, 2, 9, 9, 9,-2,-3,-3]))

