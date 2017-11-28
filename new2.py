import itertools
from itertools import groupby
from operator import itemgetter

list_graphs = []


def generate_all_graphs(number_nodes, degree_sequence_list):
    list_of_nodes = range(1, number_nodes + 1)
    zipped_list = list(zip(degree_sequence_list, list_of_nodes))
    print zipped_list
    list_edges_combinations = []
    print f(zipped_list, list_edges_combinations, level=0)
    print list_edges_combinations
    combine(list_edges_combinations, list_graphs)


def f(zipped_list, list_edges_combinations, level):
    degree = zipped_list[0][0]
    node = zipped_list[0][1]
    list1, list2 = zip(*zipped_list)
    zipped_list.pop(0)
    combination_list = list(itertools.combinations(list(list2)[1:], degree))
    temp = [zipped_list for _ in range(len(combination_list))]
    zipped_temp = zip(combination_list, temp)
    print "zipped_temp ", zipped_temp
    for i, t in enumerate(zipped_temp):
        comb_list = t[0]
        zipped_comb = t[1]
        zipped_comb = [(d - 1, n) if n in list(comb_list) else (d, n) for (d, n) in zipped_comb]
        zipped_comb = [(d, n) for (d, n) in zipped_comb if d != 0]
        zipped_temp.pop(i)
        zipped_temp.insert(i, (comb_list, zipped_comb))
    print "zipped_ temp ", zipped_temp
    for i, k in enumerate(zipped_temp):
        if not k[1]:
            list_edges = []
            for j in range(0, degree):
                list_edges.append((node, k[0][j]))
                list_edges_combinations.append((list_edges, level))
        else:
            count = len(k[1][1:])
            degree1 = k[1][0][0]
            if count < degree1:
                continue
            else:
                list_edges = []
                for j in range(0, degree):
                    list_edges.append((node, k[0][j]))
                list_edges_combinations.append((list_edges, level))
                f(k[1], list_edges_combinations, level + 1)


def combine(list_edges_combinations, list_graphs):
    for key, group in groupby(enumerate(list_edges_combinations), lambda (index, item): index - item[1]):
        group = map(itemgetter(1), group)
        list_graphs.append(group)
    print list_graphs

    for i, g in enumerate(list_graphs):
        last_index = -1
        if g[0][1] != 0:
            for j, k in enumerate(list_graphs[:i]):
                if list_graphs[j][0][1] == 0:
                    last_index = j
        list_graphs[i] = list_graphs[last_index][:g[0][1]] + list_graphs[i]
    print list_graphs

    list_graphs = [[f for (f, g) in list] for list in list_graphs]
    print list_graphs

    all_possible_graphs = []
    for list in list_graphs:
        a = []
        for l in list:
            a.extend(l)
        print a
        all_possible_graphs.append(a)

    print all_possible_graphs

# degree_sequence = input("Give a degree sequence to generate all possible graphs:")
degree_sequence = [3, 2, 1, 2, 2]
number_of_nodes = len(degree_sequence)
summation = sum(degree_sequence)
if summation % 2 == 0:
    generate_all_graphs(number_of_nodes, degree_sequence)
else:
    print "degree sequence is not satisfiable"
