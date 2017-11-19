import numpy as np
import networkx as nx
import itertools

list_graphs = []


def generate_all_graphs(number_nodes, degree_sequence_list):
    degree_sequence_list = sorted(degree_sequence_list, reverse=True)
    list_of_nodes = (range(1, number_nodes + 1))
    zipped_list = list(zip(degree_sequence_list, list_of_nodes))
    degree_to_zero(zipped_list)


def degree_to_zero(zipped_list):
    for i, num in enumerate(zipped_list):
        degree = zipped_list[i][0]
        node = zipped_list[i][1]
        zipped_list.pop(i)
        zipped_list.insert(i, (0, node))
        list1, list2 = zip(*zipped_list)

        temp = zipped_list
        count = np.count_nonzero(list1)
        if count > 1:
            combination_list = list(itertools.combinations(list2[i:], degree))
        else:
            continue
        for j, node_lists in enumerate(combination_list):
            g = nx.Graph()

            for k in range(0, degree):
                g.add_edge(node, node_lists[k])
                generate_graph(node_lists[k], temp)
            degree_to_zero(temp)
            list_graphs.append(g)


def generate_graph(node_list, temp):
        for index, z in enumerate(temp):
            if z[1] == node_list:
                d = z[0]
                n = z[1]
                temp.pop(index)
                temp.insert(index, (d - 1, n))
        return temp


degree_sequence = input("Give a degree sequence to generate all possible graphs:")
number_of_nodes = len(degree_sequence)
summation = sum(degree_sequence)
if summation % 2 == 0:
    generate_all_graphs(number_of_nodes, degree_sequence)
else:
    print "degree sequence is not satisfiable"
