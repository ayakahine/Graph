import numpy as np

# [5, 4, 4, 3, 3, 3]
# [4, 4, 3, 3, 3, 1]
# [5, 5, 3, 3, 2, 2]
# [4, 4, 3, 3, 2, 2]
# [2, 2, 1, 1, 1, 1]
# [4, 4, 3, 3, 2, 2]

# [5, 5, 2, 2, 1, 1]
# [5, 4, 4, 4, 2, 1]
# [5, 5, 5, 5, 5, 3]
# [5, 5, 3, 3, 3, 1]


def is_satisfiable(number_of_nodes, list1):
    list1 = sorted(list1, reverse=True)
    for i, num in enumerate(list1):
        temp = list1[i]
        list1[i] = 0
        count = np.count_nonzero(list1)
        if count < temp:
            print "list is unsatisfiable"
            break
        for j in xrange(i+1, i + temp + 1):
            c = list1[j]
            list1.pop(j)
            list1.insert(j, c - 1)
        list1[i + 1:] = sorted(list1[i + 1:], reverse=True)
        if list1 == [0] * number_of_nodes:
            print "list is satisfiable"
            break


number_of_nodes = input("Give the number of nodes: ")
list1 = []
while (number_of_nodes != len(list1)):
    list1 = input("Give a degree sequence of to check if it is satisfiable or not:")
is_satisfiable(number_of_nodes, list1)
