def satisfiable(degree_distribution):
    n = len(degree_distribution)
    if sum(degree_distribution) % 2 != 0:
        print "A"
        return
    for d in degree_distribution:
        if d > n or d < 1:
            print "B"
            return
    if degree_distribution.count(n - 1) > min(degree_distribution):
        print "C"
        return
    if degree_distribution.count(n - 1) and degree_distribution.count(n - 2)\
            and degree_distribution.count(1) >= 2:
        print "D"
        return
    if degree_distribution.count(n - 2) >= 3 and degree_distribution.count(1) > 1:
        print "E"
        return
    if degree_distribution.count(n - 2) >= 2 and degree_distribution.count(1) > 2:
        print "E"
        return
    if degree_distribution.count(n - 1) == 2 and degree_distribution.count(n - 2)\
            and degree_distribution.count(2) > 1:
        print "G"
        return
    if degree_distribution.count(n - 1) and degree_distribution.count(n - 3) and degree_distribution.count(1) > 2:
        print "H"
        return
    if degree_distribution.count(n - 1) and degree_distribution.count(n - 2) >= 2 and degree_distribution.count(2):
        print "I"
        return
    print "yes"


# main program
degree_sequence = [5, 4, 4, 2, 2, 1]
satisfiable(degree_sequence)
