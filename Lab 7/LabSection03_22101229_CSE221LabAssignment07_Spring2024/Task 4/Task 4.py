
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        p,r=[int(i) for i in f.readline().split()]
        cent=[int(i) for i in f.readline().split()]

        def sum(y,r):
            if r==0:
                return 0
            if r<0:
                return float("inf")
            least=float("inf")
            for i in y:
                least=min(least,1+sum(y,r-i))
            return least

        with open(output_file_path,"w") as f1:
            f1.write(str(sum(cent,r)))
            f1.close()

input_files=["input4.1.txt","input4.2.txt"]
output_files=["output4.1.txt","output4.2.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)



# The code defines a function run_code that takes paths to input and output files as arguments. Within this function,
# it opens the input file and reads integers p and r, representing the target amount and the number of denominations
# respectively, followed by a list of denominations. It then defines a recursive function sum to find the minimum number
# of coins needed to make up the target amount using the given denominations, recursively exploring all possible
# combinations. Finally, it writes the result to the output file. Outside the function, it iterates through input and
# output file pairs, calling run_code for each pair.

