from itertools import combinations_with_replacement


def generate(length, upper_bound):
    a = [map(int, comb) for comb in combinations_with_replacement(range(upper_bound,0,-1), length)]
    return a


print generate(4, 3)
