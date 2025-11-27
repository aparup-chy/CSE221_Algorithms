
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        v,e,k=[int(i) for i in f.readline().split()]
        out=[[] for i in range(v+1)]
        for i in range(e):
            n,m=[int(i) for i in f.readline().split()]
            out[n].append(m)
            out[m].append(n)

        gap=[float("inf")]*(v+1)
        queue=[]
        parent=[0]*(v+1)
        def distance_BFS(G,s):
            queue.append((s,0))
            gap[s]=0
            while queue:
                s, d = queue.pop(0)
                for i in G[s]:
                    if gap[i]>d+1:
                        parent[i]=s
                        gap[i]=d+1
                        queue.append((i,d+1))
        distance_BFS(out,1)

    with open(output_file_path,"w") as f1:
        f1.write("Time: ")
        f1.write(str(gap[k]))
        f1.write("\n")
        f1.write("Shortest Path: ")
        def path(parent,h):
            if parent[h]==0:
                f1.write(str(h))
                f1.write(" ")
                return
            path(parent,parent[h])
            f1.write(str(h))
            f1.write(" ")
        path(parent,k)
        f.close()
        f1.close()

input_files=["input5.1.txt","input5.2.txt","input5.3.txt","input5.4.txt","input5.5.txt"]
output_files=["output5.1.txt","output5.2.txt","output5.3.txt","output5.4.txt","output5.5.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# Used a parent updater incase one find short path from a node and updated distance of each node using BFS algorithm.
# Then backtraced with the help of parent list.
