
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        v,e=[int(i) for i in f.readline().split()]
        out=[[] for i in range(v+1)]
        for i in range(e):
            n,m=[int(i) for i in f.readline().split()]
            out[n].append(m)
            out[m].append(n)

    with open(output_file_path, "w") as f1:
        color=[0]*(v+1)
        def DFS(G,u):
            f1.write(str(u))
            f1.write(" ")
            color[u]+=1
            for i in G[u]:
                if color[i] == 0:
                    DFS(G,i)
        DFS(out,1)
        f.close()
        f1.close()

input_files=["input3.1.txt","input3.2.txt","input3.3.txt","input3.4.txt"]
output_files=["output3.1.txt","output3.2.txt","output3.3.txt","output3.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# Used DFS algorithm for traversing the city graph.
