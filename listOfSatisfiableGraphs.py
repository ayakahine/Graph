import numpy as np
import itertools


def generate_all_satisfiable_graphs(number_nodes, degree_sequence_list):
    list_of_nodes = range(1, number_nodes + 1)
    zipped_list = list(zip(degree_sequence_list, list_of_nodes))
    print zipped_list
    satisfiable_graphs(zipped_list)


def satisfiable_graphs(zipped_list):
    degree = zipped_list[0][0]
    node = zipped_list[0][1]
    list1, list2 = zip(*zipped_list)
    count = np.count_nonzero(list1[1:])
    if count < degree:
        return "degree sequence unsatisfiable"
    zipped_list.pop(0)
    combination_list = list(itertools.combinations(list(list2)[1:], degree))
    temp = [zipped_list for _ in range(len(combination_list))]
    zipped_temp = zip(combination_list, temp)
    print "zipped_temp ", zipped_temp
    # list_edges = [[] for _ in range(len(zipped_temp))]
    list_edges, zipped_temp = update_degree(zipped_temp, node)
    print list_edges
    print "zipped_temp after ", zipped_temp
    zipped_temp_list1, zipped_temp_list2 = zip(*zipped_temp)
    zipped_temp_list2 = [[k for k in l if k[0] != 0] for l in zipped_temp_list2]
    print "without zero", zipped_temp_list2


def update_degree(zipped_temp, node):
    list_edges = [[] for _ in range(len(zipped_temp))]
    for i, t in enumerate(zipped_temp):
        comb_list = t[0]
        zipped_comb = t[1]
        zipped_comb = [(d - 1, n) if n in list(comb_list) else (d, n) for (d, n) in zipped_comb]
        zipped_temp.pop(i)
        zipped_temp.insert(i, (comb_list, zipped_comb))
        for j in comb_list:
            list_edges[i].append((node, j))
    return list_edges, zipped_temp


# degree_sequence = input("Give a degree sequence to generate all possible graphs:")
degree_sequence = [3, 2, 1, 2, 2]
number_of_nodes = len(degree_sequence)
summation = sum(degree_sequence)
if summation % 2 == 0:
    generate_all_satisfiable_graphs(number_of_nodes, degree_sequence)
else:
    print "degree sequence is not satisfiable"
