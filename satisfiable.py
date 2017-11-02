import itertools

list_permutations = []


def generate_sequences(n, seq):
    for p in itertools.product(seq, repeat=n):
        summation = sum(p)
        if summation % 2 == 0:
            list_permutations.append(p)
    print(list_permutations)
    for pair in list_permutations:
        for j in list_permutations:
            if j != pair and j in list(itertools.permutations(pair)):
                list_permutations.remove(j)
    print(list_permutations)
    print(len(list_permutations))


while True:
    number_of_nodes = input("Give the number of nodes?")
    if number_of_nodes == "exit":
        break
    generate_sequences(number_of_nodes, range(1, number_of_nodes))
