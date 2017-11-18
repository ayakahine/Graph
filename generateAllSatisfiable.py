import numpy as np
import networkx as nx
import itertools

list_graphs = []


def generate_all_graphs(number_nodes, degree_sequence_list):
    degree_sequence_list = sorted(degree_sequence_list, reverse=True)

    list_of_nodes = (range(1, number_nodes + 1))
    zipped_list = list(zip(degree_sequence_list, list_of_nodes))
    for i, num in enumerate(zipped_list):
        degree = zipped_list[i][0]
        node = zipped_list[i][1]
        zipped_list.pop(i)
        zipped_list.insert(i, (0, node))
        list1, list2 = zip(*zipped_list)
        count = np.count_nonzero(list1)
        if count < degree:
            return "list is unsatisfiable"
        combination_list = list(itertools.combinations(list2[i:], degree))
        for j, node_lists in enumerate(combination_list):
            if i == 0:
                g = nx.Graph()
                list_graphs.append(g)

            for k in range(1, degree + 1):
                list_graphs[j].add_edge(node, node_lists[k])
            generate_graph(node_lists, zipped_list)


def generate_graph(node_lists, zipped_list):
    for index, z in enumerate(zipped_list):
        if z[1] == node_lists[1]:
            d = z[0]
            n = z[1]
            zipped_list.pop(index)
            zipped_list.insert(index, (d - 1, n))


degree_sequence = input("Give a degree sequence to generate all possible graphs:")
number_of_nodes = len(degree_sequence)
print generate_all_graphs(number_of_nodes, degree_sequence)
