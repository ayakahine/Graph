import itertools
import numpy as np
import networkx as nx


def generate_all_graphs(number_nodes, degree_sequence_list):
    # degree_sequence_list = sorted(degree_sequence_list, reverse=True)
    list_of_nodes = (range(1, number_nodes + 1))
    zipped_list = list(zip(degree_sequence_list, list_of_nodes))
    print zipped_list
    zipped_list = [(d, n) for (d, n) in zipped_list if d != 0]
    a, b = f(zipped_list)
    print "zipped list: ", a
    print "combination list: ", b


def f(zipped_list):
    list_graphs = []
    degree = zipped_list[0][0]
    node = zipped_list[0][1]
    list1, list2 = zip(*zipped_list)
    count = np.count_nonzero(list1[1:])
    if count < degree:
        return "degree sequence unsatisfiable"
    zipped_list.pop(0)
    # zipped_list.insert(0, (0, node))
    combination_list = list(itertools.combinations(list(list2)[1:], degree))
    temp = [zipped_list for _ in range(len(combination_list))]
    print temp
    zipped_temp = zip(combination_list, temp)
    print zipped_temp
    for i, t in enumerate(zipped_temp):
        g = nx.Graph()
        list_graphs.append(g)
        for j in range(0, degree):
            list_graphs[i].add_edge(node, t[0][j])
        comb_list = t[0]
        zipped_comb = t[1]
        # zipped_temp.pop()
    print [g.edges for g in list_graphs]

    return zipped_list, combination_list


# degree_sequence = input("Give a degree sequence to generate all possible graphs:")
degree_sequence = [3, 3, 2, 1, 1]
number_of_nodes = len(degree_sequence)
summation = sum(degree_sequence)
if summation % 2 == 0:
    generate_all_graphs(number_of_nodes, degree_sequence)
else:
    print "degree sequence is not satisfiable"
