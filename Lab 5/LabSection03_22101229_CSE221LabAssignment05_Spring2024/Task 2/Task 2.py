
def DFS(graph,node,sortednodes):
    graph[node]["visited"]=True
    for i in graph[node]["Adj"]:
        graph[i]["Indgree"]-=1
        if graph[i]["visited"]==False:
            DFS(graph,i,sortednodes)
    sortednodes.insert(0,node)

def topological_sort(graph,a,lst):
    sortednodes=[]
    for i in lst:
        if graph[i]["Indgree"]==0 and not graph[i]["visited"]:
            DFS(graph,i,sortednodes)
    return sortednodes

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        a,b=list(map(int,f.readline().strip().split(" ")))
        graph={}
        indgree=[0]*(a+1)
        nodelist=[]
        for i in range(1,a+1):
            nodelist.append(i)

        for i in range(a):
            graph[i+1]={"Adj":[],"Indgree":0,"visited":False}

        for i in range(b):
            x,y=list(map(int,f.readline().strip().split(" ")))
            graph[x]["Adj"].append(y)
            graph[y]["Indgree"]+=1

        for i in range(len(nodelist)):
            if graph[nodelist[i]]["Indgree"]==0:
                nodelist.insert(0,nodelist[i])
                nodelist.pop(i+1)

        new_l=topological_sort(graph,a,nodelist)

        with open(output_file_path,"w") as f1:
            if len(new_l)==len(nodelist):
                s=""
                for i in new_l:
                    s+=str(i)+" "
                f1.write(str(s).strip())
            else:
                f1.write("IMPOSSIBLE")

input_files=["input2.1.txt","input2.2.txt","input2.3.txt"]
output_files=["output2.1.txt","output2.2.txt","output2.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# The code starts by initializing a graph and performing Depth-First Search (DFS) to sort nodes topologically.
# It reads input from files, constructs the graph, and sorts the nodes using DFS. Sorted nodes are written to the
# output file if all nodes are sorted; otherwise, "IMPOSSIBLE" is written. The code iterates through each input file,
# executing the sorting process and generating an output file for each.
