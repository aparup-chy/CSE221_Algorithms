
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        V,E=[int(i) for i in f.readline().split()]
        out=[[] for i in range(V+1)]
        for i in range(E):
            v,e,w=[int(i) for i in f.readline().split()]
            out[v].append((e,w))
        r=int(f.readline())

        gap=[float("inf")]*(V+1)
        visited=[0]*(V+1)
        def extract_min(q):
            min_val=float("inf")
            min_index=-1
            for i in range(len(q)):
                if q[i][0]<min_val:
                    min_val=q[i][0]
                    min_index=i
            return q.pop(min_index)

        def dijkstra(G,s):
            c=0
            gap[s]=0
            q=[(gap[s],s)]
            visited[s]=1
            while q:
                d,x=extract_min(q)
                for e,w in G[x]:
                    c+=1
                    if gap[x]+w<gap[e]:
                        gap[e]=gap[x]+w
                    if visited[e]==0:
                        q.append((gap[e],e))
                        visited[e]=1
                if c>=V*2:
                    return -1

        dijkstra(out,r)
        with open(output_file_path,"w") as f1:
            for i in range(1,V+1):
                if gap[i]==float("inf"):
                    gap[i]=-1
            x = dijkstra(out,r)
            if x==-1:
                f1.write(str(x))
            else:
                for i in range(1,len(gap)):
                    f1.write(str(gap[i]))
                    f1.write(" ")

input_files=["input1.1.txt","input1.2.txt"]
output_files=["output1.1.txt","output1.2.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This code applies Dijkstra's algorithm using a priority queue simulation, computes the shortest paths from
# a given source vertex 'r' and writes the results ta output files. It uses 'gap' array to track minimum
# distances and employs a custom 'extract_min' function for the priority queue. The final distances are
# written to the output file, considering '-1' for unreachable vertices.
