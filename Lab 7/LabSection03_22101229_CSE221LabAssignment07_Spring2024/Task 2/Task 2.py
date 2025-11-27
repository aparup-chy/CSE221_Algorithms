
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        import heapq as hq
        V,E=[int(i) for i in f.readline().split()]
        Q=[]
        s=[[i] for i in range(1,V+1)]
        for i in range(E):
            v,e,w=[int(i) for i in f.readline().split()]
            hq.heappush(Q,(w,v,e))

        def hold(m,n):
            for i in s:
                if m in i:
                    M=i
                if n in i:
                    N=i
            if M==N:
                return -1
            s.remove(M)
            s.remove(N)
            return s.append(M+N)

        def take(Q):
            s=0
            while Q:
                w,v,e=hq.heappop(Q)
                if hold(v,e)!=-1:
                    s+=w
            return s

    with open(output_file_path,"w") as f1:
        f1.write(str(take(Q)))
        f1.close()

input_files=["input2.1.txt","input2.2.txt"]
output_files=["output2.1.txt","output2.2.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)



# The code defines a function run_code that takes paths to input and output files as arguments. Within this function,
# it opens the input file and reads the number of vertices (V) and edges (E), then initializes a priority queue Q using
# the heapq module. It reads triplets of vertices and their corresponding weights from the input file and pushes them
# onto the priority queue. The function contains two nested functions: hold to check if adding an edge creates a cycle
# and take to calculate the total weight of the minimum spanning tree using Prim's algorithm. Finally, it writes the
# total weight to the output file. Outside the function, it iterates through input and output file pairs, calling
# run_code for each pair.

