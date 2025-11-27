
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        import heapq as hq
        V,E=[int(i) for i in f.readline().split()]
        ties=[]
        fix=[[i] for i in range(1, V + 1)]
        for i in range(E):
            v,e,w=[int(i) for i in f.readline().split()]
            hq.heappush(ties,(w,v,e))

        def mini(G):
            gap=float("-inf")
            while ties:
                d,v,e=hq.heappop(ties)
                s=setting(fix,v,e)
                if s==None:
                    if gap<d:
                        dis=d
            return dis

        def setting(fix,a,b):
            for i in fix:
                if a in i:
                    A=i
                if b in i:
                    B=i
            if A==B:
                return -1
            else:
                fix.remove(A)
                fix.remove(B)
                fix.append(A+B)

        with open(output_file_path,"w") as f1:
            f1.write(str(mini(ties)))

input_files=["input3.1.txt","input3.2.txt"]
output_files=["output3.1.txt","output3.2.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# This code uses Kruskal's algorithm and performs a modified minimum spanning tree construction using a heap ('heapq').
# It combines vertices into sets, arranging them based on edge weights and calculates the minimum weight of the minimum
# spanning tree.  The result is written to the output file. The process is repeated for multiple files, generating corresponding
# output files result.

