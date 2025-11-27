
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        n,m=[int(i) for i in f.readline().split()]
        adjlist=[[0 for x in range(n+1)] for i in range(n+1)]
        for i in range(m):
            j = f.readline().split()
            a,b,c = j
            adjlist[int(a)][int(b)] = int(c)

    with open(output_file_path,"w") as f1:
        for k in adjlist:
            for m in range(len(k)):
                f1.write(f'{k[m]} ')
            f1.write("\n")
        f.close()
        f1.close()

input_files=["input1A.1.txt","input1A.2.txt"]
output_files=["output1A.1.txt","output1A.2.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# Created a 2D list of zeros for performing adjacency matrix.
