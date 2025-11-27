
def BFS(graph, start):
    visited=[False]*(len(graph)+1)
    indegree=[0]*(len(graph)+1)

    for node in graph:
        for neighbor in graph[node]["Adj"]:
            indegree[neighbor]+=1

    queue=[]
    for node in start:
        if indegree[node]==0:
            queue.append(node)
            visited[node]=True

    sortednodes=[]
    while queue:
        node=queue.pop(0)
        sortednodes.append(node)

        for neighbor in graph[node]["Adj"]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0 and not visited[neighbor]:
                queue.append(neighbor)
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
        new_l=BFS(graph, k)

        with open(output_file_path,"w") as f1:
            if len(new_l)==len(node_list):
                s=" ".join(map(str,new_l))
                f1.write(str(s).strip())
            else:
                f1.write("IMPOSSIBLE")

input_files=["input1B.1.txt","input1B.2.txt","input1B.3.txt"]
output_files=["output1B.1.txt","output1B.2.txt","output1B.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# The code initializes lists for visited nodes and node indegrees, calculates indegrees, and identifies starting nodes
# with zero indegree. It performs BFS topological sorting, dequeuing nodes, updating indegrees, and enqueuing unvisited
# nodes. Sorted nodes are written to the output file if all nodes are sorted; otherwise, "IMPOSSIBLE" is written. File
# handling reads input, constructs the graph, sorts, and writes output. It executes this process for each input file,
# generating an output file for each.
