import itertools
import numpy as np

list_permutations = []


def generate_sequences(n, seq):
    for p in itertools.product(seq, repeat=n):
        summation = sum(p)
        if summation % 2 == 0:
            list_permutations.append(p)
    print(list_permutations)
    print(len(list_permutations))

    list_permutations_sorted = [sorted(tuple(x), reverse=True) for x in list_permutations]
    unique_permutation_lists = [list(x) for x in set(tuple(x) for x in list_permutations_sorted)]
    print(unique_permutation_lists)
    print len(unique_permutation_lists)

    new_list = []
    for a, list1 in enumerate(unique_permutation_lists):
        temp = unique_permutation_lists[a]
        if is_satisfiable(number_of_nodes, list1) == "list is satisfiable":
            new_list.append(temp)
    print new_list
    print len(new_list)

def is_satisfiable(number_of_nodes, list1):
    list1 = sorted(list1, reverse=True)
    for i, num in enumerate(list1):
        temp = list1[i]
        list1[i] = 0
        count = np.count_nonzero(list1)
        if count < temp:
            return "list is unsatisfiable"
            #break
        for j in xrange(i+1, i + temp + 1):
            c = list1[j]
            list1.pop(j)
            list1.insert(j, c - 1)
        list1[i + 1:] = sorted(list1[i + 1:], reverse=True)
        if list1 == [0] * number_of_nodes:
            return "list is satisfiable"
            #break


number_of_nodes = input("Give the number of nodes?")
generate_sequences(number_of_nodes, range(1, number_of_nodes))

