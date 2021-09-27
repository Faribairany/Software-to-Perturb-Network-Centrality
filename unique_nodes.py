import csv
node_list=[]
if __name__ == '__main__':    
    filename='Cit-HepTh.txt'
    edges=[]
     #reading the input file 
    with open(filename, newline = '') as games:                                                                                          
            game_reader = csv.reader(games, delimiter='\t')
            for game in game_reader:
                
                exist=game[0] in edges
                if exist==False:
                    node_list.append(int(game[0]))
                
                
                exist=game[1] in edges
                if exist==False:
                    node_list.append(int(game[1]))  
            
              #  list1.append(game)
    res = []
    [res.append(x) for x in node_list if x not in res]
    node_list=res

    #print(max(node_list))

    dict={}
    i=0
    for val in node_list:
        i=i+1
        dict[val]=i

    print('ok')
    
    edge_list=[]
    #reading the input file 
    with open(filename, newline = '') as games:                                                                                          
            game_reader = csv.reader(games, delimiter='\t')
            for game in game_reader: 
                val1=dict[int(game[0])]  
                print(val1)
               # print((dict[int(game[0])], dict[int(game[1]])))
                edge_list.append((dict[int(game[0])], dict[int(game[1])]))
                
    

    outfile_name="cithepth_out.txt"
    for val in edge_list:
        file1 = open(outfile_name,"a") 
        file1.write(str(val[0]))
        file1.write("\t")
        file1.write(str(val[1]))
        file1.write("\n") 
                 
    print('ok')