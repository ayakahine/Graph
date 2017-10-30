import networkx as nx
import matplotlib.pyplot as plt
from random import *
import random
from operator import itemgetter
from math import ceil


def calculate_size_of_sampling(zipped_list, fraction_factor):
   C = sum([pair[0] for pair in zipped_list])
   size_of_sampling = ceil(C * fraction_factor)
   return size_of_sampling


def calculate_number_of_nodes_in_left(zipped_list, size_of_sampling):
   summation = 0
   for i, (degree,node) in enumerate(zipped_list):
      summation += degree
      if(summation >= size_of_sampling):
         break
   return i, summation


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

         while (random_node[0] == 0):
            random_node = random.choice(list_of_nodes_temp)

         g.add_edge(random_node[1], zipped_list[i][1])
         index_node = list_of_nodes_temp.index(random_node)
         d1 = zipped_list[index_node][0]
         n1 = zipped_list[index_node][1]
         zipped_list.pop(index_node)
         zipped_list.insert(index_node, (d1 - 1, n1))
         break
      else:
         random_node = random.choice(list_of_nodes_temp)

         while(random_node[0] == 0):
            random_node = random.choice(list_of_nodes_temp)

         g.add_edge(random_node[1], zipped_list[i][1])
         index_node = list_of_nodes_temp.index(random_node)
         d1 = zipped_list[index_node][0]
         n1 = zipped_list[index_node][1]
         zipped_list.pop(index_node)
         zipped_list.insert(index_node, (d1 - 1, n1))
         list_of_nodes_temp.pop(index_node)
         list_of_nodes_temp.insert(index_node, (d1 - 1, n1))
         list_of_nodes_temp.append((zipped_list[i][0], zipped_list[i][1]))
   return zipped_list

#main program
fraction_factor = 0.3
g = nx.Graph()
g.add_nodes_from(range(1,11))
degree_sequence = [3, 8, 2, 3, 2, 4, 3, 2, 4, 2]
zipped_list = tree_path(g, degree_sequence)
print("The zipped after: ", zipped_list)
zipped_list[:] = [(degree, node) for (degree, node) in zipped_list if degree != 0]
print("Zipped non-zero:  ", zipped_list)
zipped_list.sort(key= lambda zipped_list: zipped_list[0], reverse=True)
print("The sorted zipped:", zipped_list)

size_of_sampling = calculate_size_of_sampling(zipped_list, fraction_factor)
print(size_of_sampling)
NL, summation = calculate_number_of_nodes_in_left(zipped_list, size_of_sampling)
print(NL)
print(summation)

random_sample = random.sample(zipped_list, summation)
random_sample_nodes = []
for (degree, node) in random_sample:
   random_sample_nodes.append(node)
print("Ranom sample: ", random_sample_nodes)


'''for i, (degree, node) in enumerate(zipped_list):
   print(i, degree, node)
   for j, random_node in enumerate(random_sample_nodes):
      if(j < NL):
         g.add_edge(node, random_node)
'''
nx.draw(g, node_color="cyan", with_labels="true")
plt.show()
