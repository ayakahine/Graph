import random


def degree_distribution(length, upper_bound):
    if length == 0:
        return []
    else:
        return [random.randint(1, upper_bound)] + degree_distribution(length - 1, upper_bound)


def generate_degree_distribution(length, upper_bound):
    result = degree_distribution(length, upper_bound)
    result.sort(reverse=True)
    return result


print generate_degree_distribution(5, 4)
