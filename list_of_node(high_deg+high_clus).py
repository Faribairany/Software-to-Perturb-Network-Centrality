import csv 
def Union(lst1, lst2,lst3,lst4): 
    final_list = list(set(lst1) | set(lst2) | set(lst3) | set(lst4)) 
    #print()
    return final_list 

#function to convert string to int
def string_to_int(test_list):
    # perform conversion 
    test_list = [int(i) for i in test_list]
    return test_list

def intersection(lst1, lst2): 
   # print(list(set(lst1) & set(lst2)))
   # print(len(list(set(lst1) & set(lst2))))
    return list(set(lst1) & set(lst2))

#Driver program to the above graph class
if __name__ == "__main__":
    filename='as20000102.txt'
    x = filename.split(".")
    #no of node has to be 1 more than the actual no of node
    V = 6474
    filename_degree= "deg_centrality_"+ x[0] +".txt" 
    top_twenty_deg=[]
    with open(filename_degree, newline = '') as games: 
        next(games)                                                                                         
        game_reader = csv.reader(games, delimiter='\t')
        for game in game_reader:
                top_twenty_deg.append(game[0])
                if len(top_twenty_deg)==550:
                    break

    filename_clus_coef=  x[0] +"_clustering-coefficient.txt" 
    top_twenty_clus_coef=[]
    with open(filename_clus_coef, newline = '') as games: 
        next(games)                                                                                         
        game_reader = csv.reader(games, delimiter='\t')
        for game in game_reader:
                top_twenty_clus_coef.append(game[0])
                if len(top_twenty_clus_coef)==550:
                    break

    high_deg_and_high_clus=intersection(top_twenty_deg, top_twenty_clus_coef)
    print(high_deg_and_high_clus)    