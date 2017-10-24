import networkx as nx
import matplotlib.pyplot as plt
import itertools as it
from random import *
import random
#import operator
from operator import itemgetter

def subtract_degrees(degree_sequence):
   degree_sequence[:] = [x - 2 for x in degree_sequence]
   degree_sequence[0] = degree_sequence[0] + 1
   degree_sequence[-1] = degree_sequence[-1] + 1


def first_iteration_connected_path(g):
   g.add_nodes_from(range(1,8))
   degree_sequence = [3,5,2,3,2,4,3]

   list_of_nodes = list(g.nodes)
   random.shuffle(list_of_nodes)
   print(list_of_nodes)
   g.add_path(list_of_nodes)
   subtract_degrees(degree_sequence)
   print(degree_sequence)

   degree_sequence, list_of_nodes = zip(*((x, y) for x, y in zip(degree_sequence, list_of_nodes) if x != 0))
   for a ,b in zip(degree_sequence, list_of_nodes):
       print(a, b)

   print("\n")

   initial_indexDegree_list = sorted(zip(degree_sequence, list_of_nodes), key=itemgetter(0), reverse=True)
   #print(initial_indexDegree_list)
   for a,b in initial_indexDegree_list:
       print(a, b)



g = nx.Graph()
first_iteration_connected_path(g)
nx.draw(g, node_color="cyan", with_labels="true")
plt.show()
