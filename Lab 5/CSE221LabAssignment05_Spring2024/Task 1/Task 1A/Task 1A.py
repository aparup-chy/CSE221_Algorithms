def DFS(graph,start):
    visited=[False]*(len(graph)+1)
    indegree=[0]*(len(graph)+1)

    for i in graph:
        for neighbor in graph[i]["Adj"]:
            indegree[neighbor]+=1

    stack = []
    for i in start:
        if indegree[i]==0:
            stack.append(i)
            visited[i]=True

    sortednodes=[]
    while stack:
        node=stack.pop()
        sortednodes.append(node)
        for neighbor in graph[node]["Adj"]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0 and not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor]=True
    return sortednodes

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        a,b=map(int,f.readline().strip().split())
        graph={}
        node_list=[]

        for i in range(1,a+1):
            node_list.append(i)
            graph[i]={"Adj":[],"Indgree":0}

        for i in range(b):
            x,y=map(int,f.readline().strip().split())
            graph[x]["Adj"].append(y)
            graph[y]["Indgree"]+=1

        k=[]
        l=[]
        for i in range(len(node_list)):
            if graph[node_list[i]]["Indgree"]==0:
                k.append(node_list[i])
            else:
                l.append(node_list[i])
        node_list=k+l
        new_l=DFS(graph,k)

    with open(output_file_path,"w") as f1:
        if len(new_l)==len(node_list):
            s = " ".join(map(str,new_l))
            f1.write(str(s).strip())
        else:
            f1.write("IMPOSSIBLE")

input_files=["input1A.1.txt","input1A.2.txt","input1A.3.txt"]
output_files=["output1A.1.txt","output1A.2.txt","output1A.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# The code first reads input files containing graph information, constructs a directed graph, and initializes indegree
# counts for each node. Then, it identifies starting nodes with zero indegree and performs DFS to sort the nodes topologically.
# During DFS, it updates indegrees and explores neighbors, pushing nodes with zero indegree onto a stack. Finally, it writes the
# sorted nodes to an output file or "IMPOSSIBLE" if cycles are detected, ensuring a valid topological ordering.
