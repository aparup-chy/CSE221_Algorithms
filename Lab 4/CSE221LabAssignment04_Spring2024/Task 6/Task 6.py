
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        row,col=[int(i) for i in f.readline().split()]
        newl=[]
        for i in range(row):
            v=f.readline().strip()
            newl.append(v)
        d = []
        def DFS(i, j):
            if j>len(newl[0])-1 or i>len(newl)-1 or j<0 or i<0:
                return
            if v[i][j]!=0 or newl[i][j]=='#':
                return
            if newl[i][j]=='D':
                c[0]+=1
            v[i][j]=1
            DFS(i,j+1)
            DFS(i+1,j)
            DFS(i,j-1)
            DFS(i-1,j)

    with open(output_file_path,"w") as f1:
        v=[[0 for n in range(col)] for m in range(row)]
        c=[0]
        for i in range(row):
            for j in range(col):
                DFS(i,j)
                d.append(c[0])
                v=[[0 for n in range(col)] for m in range(row)]
                c=[0]
        s=str(max(d))
        f1.write(s)
        f.close()
        f1.close()

input_files=["input6.1.txt","input6.2.txt","input6.3.txt","input6.4.txt","input6.5.txt","input6.6.txt","input6.7.txt"]
output_files=["output6.1.txt","output6.2.txt","output6.3.txt","output6.4.txt","output6.5.txt","output6.6.txt","output6.7.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# Used DFS algorithm to explore and count the number of connected regions in a grid where  '#' represents an obstacle
# and 'D' represents a special cell. Finally, writes the maximum count of connected special cells to output files.
