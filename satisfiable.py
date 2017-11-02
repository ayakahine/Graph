import itertools


list_permutations = []


def generate_sequences(n, seq):
    for p in itertools.product(seq, repeat=n):
        summation = sum(p)
        if summation % 2 == 0:
            list_permutations.append(p)
    print(list_permutations)
    print(len(list_permutations))

    list_permutations_sorted = [sorted(tuple(x)) for x in list_permutations]
    unique_permutation_lists = [list(x) for x in set(tuple(x) for x in list_permutations_sorted)]
    print(unique_permutation_lists)
    print len(unique_permutation_lists)


number_of_nodes = input("Give the number of nodes?")
generate_sequences(number_of_nodes, range(1, number_of_nodes))
