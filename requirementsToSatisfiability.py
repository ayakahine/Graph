from itertools import combinations_with_replacement


def generate(length, upper_bound):
    a = [map(int, comb) for comb in combinations_with_replacement(range(upper_bound, 0, -1), length)]
    return a


def satisfiable(degree_distribution):
    n = len(degree_distribution)
    if sum(degree_distribution) % 2 != 0:
        print "A"
        return
    for d in degree_distribution:
        if d > n or d < 1:
            print "B"
            return
    if degree_distribution.count(n - 1) > min(degree_distribution) != n - 1:
        print "C"
        return
    if degree_distribution.count(n - 1) and degree_distribution.count(n - 2)\
            and degree_distribution.count(1) >= 2 and n > 3:
        print "D"
        return
    if degree_distribution.count(n - 2) >= 3 and degree_distribution.count(1) > 1:
        print "E"
        return
    if degree_distribution.count(n - 2) >= 2 and degree_distribution.count(1) > 2:
        print "E"
        return
    if degree_distribution.count(n - 1) == 2 and degree_distribution.count(n - 2)\
            and degree_distribution.count(2) > 1 and n > 4:
        print "G"
        return
    if degree_distribution.count(n - 1) and degree_distribution.count(n - 3) and degree_distribution.count(1) > 2\
            and n > 4:
        print "H"
        return
    if degree_distribution.count(n - 1) and degree_distribution.count(n - 2) >= 2 and degree_distribution.count(1)\
            and degree_distribution.count(2) and n > 4:
        print "I"
        return
    if degree_distribution.count(n - 1) == 3 and degree_distribution.count(n - 2) and degree_distribution.count(3) > 1 \
            and n > 5:
        print "J"
        return
    if degree_distribution.count(n - 1) == 2 and degree_distribution.count(n - 3) and degree_distribution.count(2) > 2 \
            and n > 5:
        print "K"
        return
    if degree_distribution.count(n - 1) == 2 and degree_distribution.count(n - 2) >= 2 and degree_distribution.count(2)\
            and degree_distribution.count(3) > 0 and n > 5:
        print "L"
        return
    if degree_distribution.count(n - 1) and degree_distribution.count(n - 4) and degree_distribution.count(1) > 3 and n\
            > 6:
        print "M"
        return
    if degree_distribution.count(n - 3) == 3 and degree_distribution.count(1) > 3:
        print "N"
        return
    if degree_distribution.count(n - 1) and degree_distribution.count(n - 3) >= 2 and degree_distribution.count(1) == 2\
            and degree_distribution.count(2) > 0 and n > 5:
        print "0"
        return
    if degree_distribution.count(n - 2) == 1 and degree_distribution.count(n - 3) and degree_distribution.count(1)\
            >= 3 and degree_distribution.count(2) != 2 and degree_distribution.count(3) != 2 and n > 6:
        print "P"
        return
    if degree_distribution.count(n - 2) == 2 and degree_distribution.count(n - 3) and degree_distribution.count(1) == 2\
            and degree_distribution.count(3) != 2 and degree_distribution.count(n - 3) != 3 and n > 4:
        print "Q"
        return
    if degree_distribution.count(n - 2) == 3 and degree_distribution.count(1) == 1 and degree_distribution.count(2) > 1:
        print "R"
        return
    if degree_distribution.count(n - 2) >= 4 and n > 5 and ((degree_distribution.count(1) and degree_distribution.count(2)) or degree_distribution.count(2) > 2) and degree_distribution.count(n - 1) == 0:
        print "S"
        return
    if degree_distribution.count(n - 1) and (degree_distribution.count(n - 2) == 3 or degree_distribution.count(n - 2) == 4) and ((degree_distribution.count(1) and degree_distribution.count(n - 3) != 2) or (degree_distribution.count(2) == 2 and degree_distribution.count(n - 3) != 1)) and n > 6:
        print "T"
        return
    if degree_distribution.count(n - 1) == 1 and degree_distribution.count(n - 2) == 2 and degree_distribution.count(2)\
            >= 3 and degree_distribution.count(3) == 0:
        print "U"
        return
    if degree_distribution.count(n - 1) == 1 and degree_distribution.count(n - 2) == 1 and degree_distribution.count(1)\
            == 1 and degree_distribution.count(n - 3) >= 1 and degree_distribution.count(2) > 1 and n > 5:
        print "V"
        return
    print "yes"
    return "yes"


# main program
list1 = []
g = generate(7, 6)
print g
# degree_sequence = [5, 4, 4, 2, 2, 1]
for degree_sequence in g:
    if satisfiable(degree_sequence) == "yes":
        list1.append(degree_sequence)
print list1
print len(list1)
