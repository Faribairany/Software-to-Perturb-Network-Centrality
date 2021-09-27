import networkx as nx 
import csv  
import operator

#Driver program to the above graph class
if __name__ == "__main__":
    filename='as20000102.txt'
     
    x = filename.split(".")
    V =  6474    
    G = nx.Graph()
    edge_list=[]
    outfile=x[0]+"_clustering-coefficient.txt"
    #reading the input file 
    with open(filename, newline = '') as games:                                                                                          
            game_reader = csv.reader(games, delimiter='\t')
            for game in game_reader:
              #  list1.append(game)
                edge_list.append((game[0], game[1]))
    
    print(edge_list)
    G.add_edges_from(edge_list)
        
    # returns a Dictionary with clustering value of each node
    clustering_coefficient=nx.clustering(G)
    #sort keys using the values in descending order
    sorted_clustering_coefficient = dict( sorted(clustering_coefficient.items(), key=operator.itemgetter(1),reverse=True))

     #opening file for writing
    file1 = open(outfile,"w") 

    #writing the headers for the degree file
    file1.write("Node_ID")
    file1.write("\t")
    file1.write("Clustering_coefficient")
    file1.write("\n")

    nodelist=[]
    for val in sorted_clustering_coefficient :
        file1.write(str(val))
        
        file1.write("\t")
        file1.write(str(sorted_clustering_coefficient [val]))
        file1.write("\n")  
  
    
  
  

