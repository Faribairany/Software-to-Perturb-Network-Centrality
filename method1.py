import csv
import random
import numpy as np
import networkx as nx
from itertools import groupby

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


#function to write headers for a file
def write_headers_to_file_for_each_core(outfile_conn_comp):
        #writing the headers for the file with degree centrality in sedcending order and the core number
        file1 = open(outfile_conn_comp,"w")  
   
        file1.write("Core_No")
        file1.write(",")
        file1.write("No_of_high_centrality_nodes_in_the_core")
        file1.write(",")
        file1.write("No_of_not_high_centrality_nodes_in_the_core")
        # file1.write(",")
        # file1.write("Number of high centrality nodes in the innermost core")
        # file1.write(",")
        # file1.write("Number of high centrality nodes in the second innermost core")
        file1.write("\n")

#function to write values to a file for each cluster plus the number of nodes in each core
def write_to_file_for_each_core(outfile_conn_comp,core_num,num_of_high_centrality_node_list_for_the_core, num_of_not_high_centrality_node_list_for_the_core):
    file1 = open(outfile_conn_comp,"a") 

    file1.write(str(core_num))
    file1.write(",")
    file1.write(str(num_of_high_centrality_node_list_for_the_core))
    file1.write(",")
    file1.write(str(num_of_not_high_centrality_node_list_for_the_core))
    # file1.write(",")
    # file1.write(str(number_of_high_cen_in_innermost_core))
    # file1.write(",")
    # file1.write(str(number_of_high_cen_in_second_innermost_core))
    file1.write("\n") 

#find the union of two lists
def Union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    #print()
    return final_list 

def node_number(V,a):
    num=(a/100)*V
    return num

#find the intersection of two lists
def intersection(lst1, lst2): 
   # print(list(set(lst1) & set(lst2)))
   # print(len(list(set(lst1) & set(lst2))))
    return list(set(lst1) & set(lst2))


def remove_punc(test_str):
        # initializing punctuations string 
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    
    # Removing punctuations in string
    # Using loop + punctuation string
    for ele in test_str: 
        if ele in punc: 
            test_str = test_str.replace(ele, " ") 
    
    # printing result 
  #  print("The string after punctuation filter : " + test_str) 
    return test_str


def list_of_negibours(neighbour_of_element):
    if len(neighbour_of_element)==0:
        no_of_elements=0
    else:
        no_of_elements=neighbour_of_element.split()
    return no_of_elements


#this fuction findsthe neighbour list of a node from adjacency list file
def find_neigbours_list(seed_node):
    #file1 = open(outfile_neighbor_no,"r") 
    with open(outfile, newline = '') as games: 
        next(games)                                                                                         
        game_reader = csv.reader(games, delimiter='\t')
        #if there is no neighbour then the variable field will be zero
        is_there_any_neighbout=0
        for game in game_reader:
            if game[0]==seed_node:
                    is_there_any_neighbout=1
                    neighbour_list=game[1]
                    break
        if is_there_any_neighbout==0:
            neighbour_list=[]
            
    return neighbour_list

#this fuction finds the neighbour list of a node from adjacency list file
def find_neigbours(seed_node):
        #opening file for writing
    #file1 = open(outfile_neighbor_no,"r") 
    with open(outfile_neighbor_no, newline = '') as games: 
        #if there is no neighbour then the variable field will be zero
        is_there_any_neighbout=0
        next(games)                                                                                         
        game_reader = csv.reader(games, delimiter='\t')
        for game in game_reader:
                if game[0]==seed_node:
                    #variable is incremented to 1 if there is neighbour present
                    is_there_any_neighbout=1
                    neighbour=game[1]
                    break
        if is_there_any_neighbout==0:
            neighbour=0
        
    return neighbour

#find the set of nodes(ten percent) to be removed according to the algorithm
def find_subgraph_around_seed_node(node_already_added, seed_node,nodelist):  
    print(seed_node)      
    #find the list of neighbours from csv
    neighbour_list_for_seed=find_neigbours_list(seed_node)
    #print(neighbour_list_for_seed)

    #if neighbour_list_for_seed!="NULL":
        #remove the punctuation from the list
    neighbour_list_for_seed=remove_punc(neighbour_list_for_seed)
        #count the list of elements in the list
    neighbour_list_for_seed=list_of_negibours(neighbour_list_for_seed)
        # to remove duplicated 

    #from list 
    res = []
    [res.append(x) for x in neighbour_list_for_seed if x not in res]
    neighbour_list_for_seed=res
    #removing the node itself from the list
    exist=seed_node in neighbour_list_for_seed
    if exist==True:
            neighbour_list_for_seed.remove(seed_node)
    print(neighbour_list_for_seed)

    dict_node_with_neighbour_num={}
    for element in neighbour_list_for_seed:
            #find the list of neighbours from csv
            neighbour_list_for_element=find_neigbours_list(element)
            #remove the punctuation from the list
            neighbour_list_for_element=remove_punc(neighbour_list_for_element)
             #count the list of elements in the list
            neighbour_list_for_element=list_of_negibours(neighbour_list_for_element)
            #remove duplicates from the list if the size of list is not zero
            if neighbour_list_for_element!=0:
                # from list 
                res = []
                [res.append(x) for x in neighbour_list_for_element if x not in res]
                neighbour_list_for_element=res

           # print(element)
            if neighbour_list_for_element!=0:
                #removing the element itself from the list
                exist=element in neighbour_list_for_element
                if exist==True:
                    neighbour_list_for_element.remove(element)
           # print(neighbour_list_for_element)
           
            
            new_list=[]
            if neighbour_list_for_element!=0:
            #find all the neighbours that are not added to the already added node list
             for val in neighbour_list_for_element:
                exist=val in node_already_added
                if exist==False:
                    new_list.append(val)
            #count_no_of_negibours split the string with space put elements in a list and count the number of elements
            dict_node_with_neighbour_num[element]=int(len(new_list))
        
    list_of_keys_to_be_removed_from_dict=[]
        #remove the elements from the dict for which the key is already present in node already added list
    for keys in dict_node_with_neighbour_num:
            exist=keys in node_already_added
            if exist==True:
                list_of_keys_to_be_removed_from_dict.append(keys)
                
    # Remove multiple keys from dictionary
    [dict_node_with_neighbour_num.pop(key) for key in list_of_keys_to_be_removed_from_dict]
        #print(neighbour_number)
    if len(dict_node_with_neighbour_num.keys())!=0:
            next_node_to_be_added=max(dict_node_with_neighbour_num, key=dict_node_with_neighbour_num.get)
    else:
            #no node exists that can be added to the next node list, reaches to an edge point, this happaens for highly connected subgraph
            next_node_to_be_added="NULL"

    return  next_node_to_be_added



#return list of edges for the file
def edge_list(filename):
    list1=[]
    with open(filename, newline = '') as games:                                                                                          
            game_reader = csv.reader(games, delimiter='\t')
            for game in game_reader:
                # game.pop()
                # game.pop()
                # game.pop()
                #how to convert elements of a list to int from str
                game = [int(i) for i in game]
                #converting game from list to tuple
                #game=tuple(game)
                #converting element of a tuple to int
            # game = tuple(int(num) for num in game.replace('(', '').replace(')', '').split(', ')) 
                list1.append(game)
                #adj = {k: [v[1] for v in g] for k, g in groupby(sorted(list1), lambda e: e[0])}
    #graph=list1
    return list1

#return associated edge list for a set of nodes
def connected_comp(outfile_modified_edge_list,graph,num):        
       # x = filename.split(".")
       # outfile=x[0]+"_edgelist_after_removing-n_percent_node.txt"
        #python function that will return a list of edges whose both elements are present in the num list(will return the connected component)
        file = open(outfile_modified_edge_list,"w")  
        connect_comp=[]
        for element in graph:
            if element[0] in num and element[1] in num:
                connect_comp.append(element)
                file.write(str(element[0]))
                file.write("\t")
                file.write(str(element[1]))
                #file1.write("\t")
                #file1.write("Core_Number")
                file.write("\n")
        return connect_comp

#G = nx.read_edgelist(filename,create_using=nx.Graph(), nodetype = int)
def high_centrality_nodes(filename):
    x = filename.split(".")
    #reading the input file 
    top_twenty_close=[]
    filename_close= "close_centrality_"+ x[0] +".txt" 
    with open(filename_close, newline = '') as games: 
        next(games)                                                                                         
        game_reader = csv.reader(games, delimiter='\t')
        for game in game_reader:
                top_twenty_close.append(game[0])
                if len(top_twenty_close)==20:
                    break

    #print(top_twenty_close)

    #reading the input file 
    top_twenty_between=[]
    filename_bet= "bet_centrality_"+ x[0] +".txt" 
    with open(filename_bet, newline = '') as games: 
        next(games)                                                                                         
        game_reader = csv.reader(games, delimiter='\t')
        for game in game_reader:
                top_twenty_between.append(game[0])
                if len(top_twenty_between)==20:
                    break
        #find the list of node either in top twenty high closeness or betweeneess centrality
    high_centrality_node=Union(top_twenty_close, top_twenty_between)
    #convert all the elements of nested list to int
    high_centrality_node = [int(i) for i in high_centrality_node] 
    return high_centrality_node

def str_to_int(test_list):
        # using naive method to
    # perform conversion
    for i in range(0, len(test_list)):
        test_list[i] = int(test_list[i])
    return test_list


#function to put all values of a dict to a list
def unique_values_dict(dic):
    list_val=[]
    for keys in dic: 
        list_val.append(dic[keys])
    unique_list=list(set(list_val))
    return unique_list


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
    #no of node has to be 1 more than the actual no of node
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
    
   # write_neighbour_info_to_file(outfile,outfile_node,outfile_neighbor_no,adjacency_list)
    
    nodelist=[]
    for val in adjacency_list: 
        nodelist.append(val)  

    
    #Method1(Randomly choose a node and increment the size of the graph choose a neighbour with highest no of neighbours), in this way continue until 10% nodes are includes in the subgraph 
    #['2708','1407','557','1','1394']
    #each time use one seed from the list
    seed_node='59'
    #print(seed_node)

    #calculate the number of adjacency nodes to be removed from the list
    N_percent_no_num=node_number(V,10)

    #list of nodes added to the number of nodes to be removed
    node_already_added=[]
    node_already_added.append(seed_node)

    node_in_the_n_percent_node_list=[]
    node_in_the_n_percent_node_list=node_already_added

    #the loop contains while the node list contains n percent nodes
    while(len(node_already_added)!=int(N_percent_no_num)):
    #    print(len(node_already_added))
      
            next_node=find_subgraph_around_seed_node(node_already_added,seed_node,nodelist)
            if next_node==730:
                print('ok')

            seed_node=next_node
            exist=next_node in node_already_added
            if next_node!="NULL" and exist==False:
                node_already_added.append(next_node)
            else:
                print('Node to exit')
                print(seed_node)
                break

    print(len(node_already_added))


   # print(node_already_added)
    #find the node not in the list
   # not_not_added_to_list=[]

   # for val in nodelist:
     #   exist=val in node_already_added
       # if exist==False:
         #   not_not_added_to_list.append(val)

    #read the input file and return the adjacency list for each node
    graph=edge_list(filename)

    #convert all the elements of list to int
    node_already_added= str_to_int(node_already_added)
    #the function is called to write the modified edge_list(edge list found after removing associated  edges of n percent node) to a file
    connected_comp(outfile_modified_edge_list,graph,node_already_added)


    #reading the modified edgelist
    G = nx.read_edgelist(outfile_modified_edge_list,create_using=nx.Graph(), nodetype = int)
    #remove self loops
    G.remove_edges_from(nx.selfloop_edges(G))
            # cc=number_connected_components(G)
            # if cc>1:
            #     list_val.append(value)

    #finding high centrality nodes in the original list
    high_cent_node=high_centrality_nodes(filename)



    #list of high centrality node in connected component
    high_centrality_node_list_for_the_conn_comp=intersection(high_cent_node, node_already_added)
    #list of not high centrality node in connected component
    not_high_centrality_node_list_for_the_conn_comp=[i for i in node_already_added if i not in high_cent_node]

    #finding the new nodelist

    #list of high centrality node in connected component
    high_centrality_node_list_for_the_conn_comp=intersection(high_cent_node, node_already_added)
    #list of not high centrality node in connected component
    not_high_centrality_node_list_for_the_conn_comp=[i for i in node_already_added if i not in high_cent_node]

    #num_of_edges_bet_nodes=connected_comp(graph,list_val)
            
    #for core number
    number_of_high_cen_in_innermost_core=0
    number_of_high_cen_in_second_innermost_core=0

    number_of_not_high_cen_in_innermost_core=0
    number_of_not_high_cen_in_second_innermost_core=0

    core_number_high_cen_node=nx.core_number(G)

    #identify list of core numbers
    unique_list_val=unique_values_dict(core_number_high_cen_node)

    #u_value = set( val for dic in core_number_high_cen_node for val in dic.values())
    # # new_list is a set of list1
    #new_list = set(u_value) 


    # finding the core number as key and list of node with the same core number as key as the value
            # from dictionary using set
    flipped = {}
    
    for key, value in core_number_high_cen_node.items():
                if value not in flipped:
                    flipped[value] = [key]
                else:
                    flipped[value].append(key)


    outfile_final=x[0]+"_core_no_and_node_info_random_seed.csv"
    write_headers_to_file_for_each_core(outfile_final)
    #cluster_no=cluster_no+1
            # #sorting the dict according to core num
    flipped=dict(sorted(flipped.items()))
            # #check the number of high cen and not high centrality nodes for each core
    for keys in flipped:
                #list of high centrality node in connected component
                high_centrality_node_list_for_the_core=intersection(high_cent_node, flipped[keys])
                num_of_high_centrality_node_list_for_the_core=len(high_centrality_node_list_for_the_core)
                #list of not high centrality node in connected component
                not_high_centrality_node_list_for_the_core=[i for i in flipped[keys] if i not in high_cent_node]
                num_of_not_high_centrality_node_list_for_the_core=len(not_high_centrality_node_list_for_the_core)
                core_num=keys
                write_to_file_for_each_core(outfile_final,core_num,num_of_high_centrality_node_list_for_the_core, num_of_not_high_centrality_node_list_for_the_core)
