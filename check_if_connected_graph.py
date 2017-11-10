import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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
        if list(list3) == [0] * number_nodes:
            if nx.is_connected(g):
                # nx.draw(g, with_labels="true")
                # plt.show()
                return "graph is connected"


# main program
number_of_nodes = input("Give the number of nodes: ")
degree_seq = input("Degree sequence: ")
print is_connected_graph(number_of_nodes, degree_seq)
