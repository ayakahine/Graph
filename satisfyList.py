import numpy as np

# [5, 4, 4, 3, 3, 3]
# [4, 4, 3, 3, 3, 1]
# [5, 5, 3, 3, 2, 2]
# [4, 4, 3, 3, 2, 2]
# [2, 2, 1, 1, 1, 1]

# [5, 5, 2, 2, 1, 1]
# [5, 4, 4, 4, 2, 1]
# [5, 5, 5, 5, 5, 3]
# [5, 5, 3, 3, 3, 1]

list1 = [4, 4, 3, 3, 2, 2]
print list1

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
        # print list1
    list1[i + 1:] = sorted(list1[i + 1:], reverse=True)
    if list1 == [0, 0, 0, 0, 0, 0]:
        print "list is satisfiable"
        break
