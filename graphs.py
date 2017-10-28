import networkx as nx
import matplotlib.pyplot as plt
from random import *
import random
from operator import itemgetter
#from functools import reduce

'''
def subtract_degrees(degree_sequence):
   degree_sequence[:] = [x - 2 for x in degree_sequence]
   degree_sequence[0] = degree_sequence[0] + 1
   degree_sequence[-1] = degree_sequence[-1] + 1



def first_iteration_connected_path(g, degree_sequence):

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
   print("\n")


def calculate_size_of_sampling(degree_sequence):
   fraction_factor = 0.3
   C = sum(degree_sequence)
   size_of_sampling = C * fraction_factor
   print(size_of_sampling)
'''

def calculate_number_of_nodes_in_left(degree_sequence, C):
   #sum(degree_sequence) <= 0.3 * C
   summation = 0
   for i, degree in enumerate(degree_sequence):
      summation += degree
      if(summation >= 0.3 * C):
         break

   print(degree_sequence[i-1])


def tree_path(g, degree_sequence):
   list_of_nodes = list(g.nodes)
   random.shuffle(list_of_nodes)
   print('The list of all nodes: ', list_of_nodes)
   print('The degree sequence', degree_sequence)

   zipped_list = list(zip(degree_sequence, list_of_nodes))
   print('The zipped list : ', zipped_list)

   g.add_edge(zipped_list[0][1], zipped_list[1][1])

   list_of_nodes_temp = list(zip([], []))
   for i, (degree, node) in enumerate(zipped_list):
      d = zipped_list[i][0]
      n = zipped_list[i][1]
      zipped_list.pop(i)
      zipped_list.insert(i, (d - 1, n))
      if(i == 0 or i == 1):
         list_of_nodes_temp.append((zipped_list[i][0], zipped_list[i][1]))
         continue
      elif(i == len(list_of_nodes) - 1):
         random_node = random.choice(list_of_nodes_temp)
         while True :
            if(random_node[0] <= 0):
               random_node = random.choice(list_of_nodes_temp)
            else:
               break
         g.add_edge(random_node[1], zipped_list[i][1])

         index = list_of_nodes_temp.index(random_node)
         d1 = zipped_list[index][0]
         n1 = zipped_list[index][1]
         zipped_list.pop(index)
         zipped_list.insert(index, (d1 - 1, n1))
         break
      else:
         random_node = random.choice(list_of_nodes_temp)
         while True :
            if(random_node[0] <= 0):
               random_node = random.choice(list_of_nodes_temp)
            else:
               break
         g.add_edge(random_node[1], zipped_list[i][1])

         index = list_of_nodes_temp.index(random_node)
         d1 = zipped_list[index][0]
         n1 = zipped_list[index][1]
         zipped_list.pop(index)
         zipped_list.insert(index, (d1 - 1, n1))

         list_of_nodes_temp.append((degree_sequence[i], list_of_nodes[i]))
   print(zipped_list)


g = nx.Graph()
g.add_nodes_from(range(1,8))
degree_sequence = [3, 5, 2, 3, 2, 4, 3]
tree_path(g, degree_sequence)

#C = sum(degree_sequence)
#calculate_number_of_nodes_in_left(degree_sequence, C)
nx.draw(g, node_color="cyan", with_labels="true")
plt.show()
