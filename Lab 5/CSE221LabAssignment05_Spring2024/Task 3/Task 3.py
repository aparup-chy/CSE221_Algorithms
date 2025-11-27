
def dfs(node,graph,stack):
    graph[node]["visited"]=True
    for i in graph[node]["Adj"]:
        if graph[i]["visited"]==False:
            dfs(i,graph,stack)
    stack.append(node)

def dfs_scc(node,graph,scc):
    graph[node]["visited"]=True
    scc.append(node)
    for i in graph[node]["Adj"]:
        if graph[i]["visited"]==False:
            dfs_scc(i,graph,scc)

def transpose(graph):
    newgraph={}
    for i in range(1,len(graph)+1):
        newgraph[i]={"Adj":[],"visited":False}

    for node in graph:
        for i in graph[node]["Adj"]:
            newgraph[i]["Adj"].append(node)
    return newgraph

def SCC(graph):
    stack=[]
    for i in range(1,len(graph)+1):
        if graph[i]["visited"]==False:
            dfs(i,graph,stack)
    scc=[]
    t_graph=transpose(graph)
    while stack:
        node=stack.pop()
        if not t_graph[node]["visited"]:
            s=[]
            dfs_scc(node,t_graph,s)
        scc.append(s)
    return scc

def remove_duplicate_sublists(input):
    output=[]
    a=set()

    for i in input:
        tup=tuple(i)
        if tup not in a:
            a.add(tup)
            output.append(i)
    return output

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        a,b=list(map(int, f.readline().strip().split(" ")))
        graph={}
        indgree=[0]*(a+1)
        nodelist = []
        for i in range(1,a+1):
            nodelist.append(i)
        for i in range(a):
            graph[i+1]={"Adj":[],"visited":False}
        for i in range(b):
            x,y=list(map(int,f.readline().strip().split(" ")))
            graph[x]["Adj"].append(y)

        with open(output_file_path, "w") as f1:
            lsit1=SCC(graph)
            final=remove_duplicate_sublists(lsit1)
            for i in final:
                print(" ".join(map(str,i)),file=f1)

input_files=["input3.1.txt","input3.2.txt","input3.3.txt"]
output_files=["output3.1.txt","output3.2.txt","output3.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# The code employs Kosaraju's algorithm to find Strongly Connected Components (SCCs) in a directed graph. Initially, it
# conducts a depth-first search (DFS) to fill a stack with nodes ordered by their finishing times. Next, it transposes
# the graph by reversing the direction of each edge. Then, it executes another DFS on the transposed graph, processing
# nodes from the stack to identify SCCs. After identifying SCCs, it removes duplicates to ensure uniqueness. Finally,
# the identified SCCs are written to the output file. This process is repeated for each input file, producing an output
# file for each input.
