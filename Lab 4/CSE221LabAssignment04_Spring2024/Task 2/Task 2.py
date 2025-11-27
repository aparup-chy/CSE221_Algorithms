
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        v,e=[int(i) for i in f.readline().split()]
        out=[[] for i in range(v+1)]
        for i in range(e):
            n,m=[int(i) for i in f.readline().split()]
            out[n].append(m)
            out[m].append(n)

    with open(output_file_path,"w") as f1:
        color=[0]*(v+1)
        queue=[]
        def BFS(G,s):
            queue.append(s)
            color[s]=1
            while queue:
                s=queue.pop(0)
                f1.write(str(s))
                f1.write(" ")
                for i in G[s]:
                    if color[i]==0:
                        queue.append(i)
                        color[i] = 1
        BFS(out,1)
        f.close()
        f1.close()

input_files=["input2.1.txt","input2.2.txt","input2.3.txt","input2.4.txt"]
output_files=["output2.1.txt","output2.2.txt","output2.3.txt","output2.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# Used BFS algorithm for traversing the city graph.
