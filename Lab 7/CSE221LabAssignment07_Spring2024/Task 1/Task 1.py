
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        V,E=[int(i) for i in f.readline().split()]
        Q=[]
        s=[[i] for i in range(1,V+1)]
        for i in range(E):
            v,e=[int(i) for i in f.readline().split()]
            Q.append((v,e))

        def set(a,b):
            for i in s:
                if a in i:
                    A=i
                if b in i:
                    B=i
            if A==B:
                return len(A)
            s.remove(A)
            s.remove(B)
            s.append(A+B)
            return len(A+B)

        with open(output_file_path,"w") as f1:
            while Q:
                v,e=Q.pop(0)
                f1.write(str(set(v,e)))
                f1.write("\n")

        f.close()
        f1.close()


input_files=["input1.1.txt","input1.2.txt"]
output_files=["output1.1.txt","output1.2.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)



# The code defines a function run_code that takes paths to input and output files as arguments. Within this function,
# it opens the input file and reads the number of vertices (V) and edges (E), then initializes a list Q and a set of
# sets, s, representing disjoint sets. It reads pairs of vertices representing edges from the input file and appends
# them to Q. The function also contains a nested function set to perform set union operations. It then iterates through
# Q, performing set union operations and writing the resulting set sizes to the output file. Finally, it closes both
# input and output files. Outside the function, it iterates through input and output file pairs, calling run_code for
# each pair.

