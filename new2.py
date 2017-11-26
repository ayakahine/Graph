import itertools

list_graphs = []


def generate_all_graphs(number_nodes, degree_sequence_list):
    list_of_nodes = range(1, number_nodes + 1)
    zipped_list = list(zip(degree_sequence_list, list_of_nodes))
    print zipped_list
    list_edges_combinations = []
    print f(zipped_list, list_edges_combinations)


def f(zipped_list, list_edges_combinations):
    degree = zipped_list[0][0]
    node = zipped_list[0][1]
    list1, list2 = zip(*zipped_list)
    zipped_list.pop(0)
    combination_list = list(itertools.combinations(list(list2)[1:], degree))
    temp = [zipped_list for _ in range(len(combination_list))]
    zipped_temp = zip(combination_list, temp)
    print "zipped_temp ", zipped_temp
    for i, t in enumerate(zipped_temp):
        list_edges = []
        for j in range(0, degree):
            list_edges.append((node, t[0][j]))
        comb_list = t[0]
        zipped_comb = t[1]
        zipped_comb = [(d - 1, n) if n in list(comb_list) else (d, n) for (d, n) in zipped_comb]
        zipped_comb = [(d, n) for (d, n) in zipped_comb if d != 0]
        zipped_temp.pop(i)
        zipped_temp.insert(i, (comb_list, zipped_comb))
        list_edges_combinations.append(list_edges)
    print "zipped_ temp ", zipped_temp

    zipped_temp_list1, zipped_temp_list2 = zip(*zipped_temp)
    print zipped_temp_list2
    for i, k in enumerate(zipped_temp_list2):
        if not k:
            continue
        else:
            count = len(zipped_temp_list2[i][1:])
            degree1 = zipped_temp_list2[i][0][0]
            if count < degree1:
                continue
            else:
                f(k, list_edges_combinations)


# degree_sequence = input("Give a degree sequence to generate all possible graphs:")
degree_sequence = [3, 2, 1, 2, 2]
number_of_nodes = len(degree_sequence)
summation = sum(degree_sequence)
if summation % 2 == 0:
    generate_all_graphs(number_of_nodes, degree_sequence)
else:
    print "degree sequence is not satisfiable"
