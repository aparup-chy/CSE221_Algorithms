
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        n=int(f.readline())
        m=[0]*(n+1)

        def toad(n):
            if n<=1:
                return 1
            if m[n]!=0:
                return m[n]
            m[n]=toad(n-1)+toad(n-2)
            return m[n]

    with open(output_file_path,"w") as f1:
        f1.write(str(toad(n)))
        f1.close()

input_files=["input3.1.txt","input3.2.txt","input3.3.txt","input3.4.txt"]
output_files=["output3.1.txt","output3.2.txt","output3.3.txt","output3.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)



# The code defines a function run_code that takes paths to input and output files as arguments. Within this function,
# it opens the input file and reads an integer n, representing the number of steps in a toad's journey. It then defines
# a recursive function toad to calculate the number of ways a toad can jump up n steps, storing previously calculated
# values in a list m to avoid redundant computations. Finally, it writes the result to the output file. Outside the
# function, it iterates through input and output file pairs, calling run_code for each pair.

