import itertools
from itertools import groupby
from operator import itemgetter
# from generateSortingDegreeDistribution import degree_sequence


def generate_all_graphs(number_nodes, degree_sequence_list):
    list_of_nodes = range(1, number_nodes + 1)
    zipped_list = list(zip(degree_sequence_list, list_of_nodes))
    list_graphs = []
    list_edges_combinations = []
    a = []
    f(zipped_list, list_edges_combinations, a, level=0)
    print list_edges_combinations
    print a
    all_graphs = combine(list_edges_combinations, list_graphs)
    return all_graphs


def f(zipped_list, list_edges_combinations, a, level):
    degree = zipped_list[0][0]
    node = zipped_list[0][1]
    list1, list2 = zip(*zipped_list)
    zipped_list.pop(0)
    combination_list = list(itertools.combinations(list(list2)[1:], degree))
    temp = [zipped_list for _ in range(len(combination_list))]
    zipped_temp = zip(combination_list, temp)
    for i, t in enumerate(zipped_temp):
        comb_list = t[0]
        zipped_comb = t[1]
        zipped_comb = [(d - 1, n) if n in list(comb_list) else (d, n) for (d, n) in zipped_comb]
        zipped_comb = [(d, n) for (d, n) in zipped_comb if d != 0]
        zipped_temp.pop(i)
        zipped_temp.insert(i, (comb_list, zipped_comb))
    for i, k in enumerate(zipped_temp):
        list_edges = []
        for j in range(0, degree):
            list_edges.append((node, k[0][j]))
        list_edges_combinations.append((list_edges, level))

        if not k[1]:
            a.append((list_edges, level, "S"))
            continue
        else:
            count = len(k[1][1:])
            degree1 = k[1][0][0]
            if count < degree1:
                a.append((list_edges, level, "F"))
                continue
            else:
                a.append((list_edges, level, "S"))
                f(k[1], list_edges_combinations, a, level + 1)


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

    list_graphs = [[c for (c, d) in list1] for list1 in list_graphs]

    all_possible_graphs1 = []
    for list1 in list_graphs:
        a = []
        for l in list1:
            a.extend(l)
        all_possible_graphs1.append(a)

    return all_possible_graphs1


# degree_sequence =[3, 2, 1, 2, 2]
# degree_sequence = [1, 1, 1, 3]
degree_sequence = [2, 2, 3, 3]
number_of_nodes = len(degree_sequence)
summation = sum(degree_sequence)
if summation % 2 == 0:
    all_possible_graphs = generate_all_graphs(number_of_nodes, degree_sequence)
    print all_possible_graphs
else:
    print "degree sequence is not satisfiable"
