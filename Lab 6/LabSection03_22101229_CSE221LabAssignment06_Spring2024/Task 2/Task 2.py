
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        V,E=[int(i) for i in f.readline().split()]
        out=[[] for i in range(V+1)]
        for i in range(E):
            v,e,w=[int(i) for i in f.readline().split()]
            out[v].append((e,w))
        Y,Z=[int(i) for i in f.readline().split()]

        import heapq as hq
        gap=[float("inf")]*(V+1)
        visited=[0]*(V+1)
        def dijkstra(G,s):
            c=0
            gap[s]=0
            q=[]
            hq.heappush(q,(gap[s],s))
            visited[s]=1
            while q:
                d,x=hq.heappop(q)
                for e,w in G[x]:
                    c+=1
                    if gap[x]+w<gap[e]:
                        gap[e]=gap[x]+w
                    if visited[e]==0:
                        hq.heappush(q,(gap[e],e))
                        visited[e]=1
                if c>=V*2:
                    return -1
            return gap

        with open(output_file_path,"w") as f1:
            gapA=dijkstra(out,Y)
            gap=[float("inf")]*(V+1)
            visited=[0]*(V+1)
            gapB=dijkstra(out,Z)
            gapcombo=[]
            for i in range(1,V+1):
                hq.heappush(gapcombo,(max(gapA[i],gapB[i]),i))
            d,v=hq.heappop(gapcombo)
            if d==float("inf"):
                f1.write("Impossibe")
            else:
                f1.write("Time ")
                f1.write(str(d))
                f1.write("\n")
                f1.write("Node ")
                f1.write(str(v))
            f1.close()

input_files=["input2.1.txt","input2.2.txt","input2.3.txt"]
output_files=["output2.1.txt","output2.2.txt","output2.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This code performs Dijkstra's algorithm using a priority queue ('heapq') for two specified source vertices, 'Y' and 'Z'.
# It then combines the computed distances for each vertex based on the information is written to the output file, including
# the minimum time and node. The process is repeated for multiple input files, generating corresponding output files.

