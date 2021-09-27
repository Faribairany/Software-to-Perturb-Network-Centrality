import csv
import random
import numpy as np
import networkx as nx


# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
 
# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
 
    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
 
    # Function to print the graph
    def print_graph(self):
        dict={}
        for i in range(self.V):
           # print("Adjacency list of vertex {}\n head".format(i), end="")
           
            temp = self.graph[i]
            list=[]
            while temp:
               # dict[i]=[format(temp.vertex)]
                list.append(temp.vertex)
               # print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            dict[format(i)]=list
           # print(" \n")
        return dict


#write adj_list
def write_neighbour_info_to_file(outfile,outfile_node,outfile_neighbor_no,adjacency_list):
    #opening file for writing
    file1 = open(outfile,"w") 
    file2 = open(outfile_node,"w")  
    file3 = open(outfile_neighbor_no,"w") 

    #writing the headers for the degree file
    file1.write("Node_ID")
    file1.write("\t")
    file1.write("Adjacent_nodes")
    file1.write("\n")

      #writing the headers for the degree file
    file3.write("Node_ID")
    file3.write("\t")
    file3.write("Neighbour_no")
    file3.write("\n")

    file2.write("Node_ID")
    file2.write("\n")
    nodelist=[]
    for val in adjacency_list:
        file1.write(str(val))
        
        file1.write("\t")
        file1.write(str(adjacency_list[val]))
        file1.write("\n")  
        #writing the nodes to  file
        file2.write(str(val))
        file2.write("\n")   
        nodelist.append(val)   
        file3.write(str(val))
        file3.write("\t")
        file3.write(str(len(adjacency_list[val])))
        file3.write("\n")  

#Driver program to the above graph class
if __name__ == "__main__":
    filename='as20000102.txt'
    x = filename.split(".")
    V = 6474
    graph = Graph(V)
    #reading the input file 
    with open(filename, newline = '') as games:                                                                                          
            game_reader = csv.reader(games, delimiter='\t')
            for game in game_reader:
              #  list1.append(game)
                graph.add_edge(int(game[0]), int(game[1]))
 
    adjacency_list=graph.print_graph()
    #print(adjacency_list)
    
    outfile=x[0]+"_adjacency_list.txt"
    outfile_neighbor_no=x[0]+"_adjacency_list_number.txt"
    outfile_modified_edge_list=x[0]+"_edgelist_after_removing-n_percent_node.txt"
    outfile_node=x[0]+"_node_list.txt"
    
    write_neighbour_info_to_file(outfile,outfile_node,outfile_neighbor_no,adjacency_list)