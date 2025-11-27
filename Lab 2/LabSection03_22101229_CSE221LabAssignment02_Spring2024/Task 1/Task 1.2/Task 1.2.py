# Using O(N) Complexity
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        with open(output_file_path,"w") as f1:
            s=f.readline().split(" ")
            N=int(s[0])
            S=int(s[1])
            arr=[int(i) for i in f.readline().split(" ")]
            sum_in={}
            found_pair=False
            for i in range(N):
                complement=S-arr[i]
                if complement in sum_in:
                    j=sum_in[complement]
                    f1.write(str(j+1)+" "+str(i+1))
                    found_pair=True
                    break
                sum_in[arr[i]]=i
            if not found_pair:
                f1.writelines("IMPOSSIBLE")

        f.close()
        f1.close()

input_files=["input1.1.txt","input1.2.txt","input1.3.txt","input1.4.txt"]
output_files=["output1.1.txt","output1.2.txt","output1.3.txt","output1.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This Python code reads an integer pair N and S from a file, followed by a list of integers arr.
# It then initializes an empty dictionary sum_in and iterates through the list. For each element,
# it calculates the complement needed to reach the target sum S. If the complement is found in the dictionary,
# it writes the indices of the pair to an output file. If no pair is found, it writes "IMPOSSIBLE" to the file.