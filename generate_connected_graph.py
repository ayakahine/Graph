import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

list_permutations = []


def generate_sequences(n, seq):
    for p in itertools.product(seq, repeat=n):
        summation = sum(p)
        if summation % 2 == 0:
            list_permutations.append(list(p))
    print(list_permutations)
    print(len(list_permutations))


    new_list = []
    for a, degree_sequence_list in enumerate(list_permutations):
        temp = list_permutations[a]
        if is_connected_graph(number_of_nodes, degree_sequence_list) == "graph is connected":
            new_list.append(temp)
    print new_list
    print len(new_list)


def is_connected_graph(number_nodes, degree_sequence_list):
    g = nx.Graph()
    g.add_nodes_from(range(1, number_nodes + 1))
    list_of_nodes = list(g.nodes)
    zipped_list = list(zip(degree_sequence_list, list_of_nodes))
    for i, num in enumerate(zipped_list):
        degree = zipped_list[i][0]
        node = zipped_list[i][1]
        zipped_list.pop(i)
        zipped_list.insert(i, (0, node))
        list1, list2 = zip(*zipped_list)
        count = np.count_nonzero(list1)
        if count < degree:
            return "graph is unconnected"
        for j in xrange(i+1, i + degree + 1):
            d = zipped_list[j][0]
            n = zipped_list[j][1]
            zipped_list.pop(j)
            zipped_list.insert(j, (d - 1, n))
            g.add_edge(node, n)
        list3, list4 = zip(*zipped_list)
        if list3 == [0] * number_nodes:
            if nx.is_connected(g):
                return "graph is connected"


# main program
number_of_nodes = input("Give the number of nodes?")
generate_sequences(number_of_nodes, range(1, number_of_nodes))
