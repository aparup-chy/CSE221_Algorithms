
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        v,e=[int(i) for i in f.readline().split()]
        out=[[] for i in range(v+1)]
        for i in range(e):
            n,m=[int(i) for i in f.readline().split()]
            out[n].append(m)

    with open(output_file_path,"w") as f1:
        color=[0]*(v+1)
        color[0]="NO"
        def cycle_dfs(G,s):
            color[s]=1
            for i in G[s]:
                if color[i] == 0:
                    cycle_dfs(G,i)
                elif color[i]==1:
                    color[0]="YES"
            color[s]=2
        cycle_dfs(out,1)
        f1.write(str(color[0]))
        f.close()
        f1.close()

input_files=["input4.1.txt","input4.2.txt","input4.3.txt","input4.4.txt","input4.5.txt"]
output_files=["output4.1.txt","output4.2.txt","output4.3.txt","output4.4.txt","output4.5.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# Used  a checker 0, 1, 2 for tracing cycle in DFS search. Stored the data in the first index of the color checker.
