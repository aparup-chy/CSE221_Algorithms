# Using O(N) Complexity

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        with open(output_file_path,"w") as f1:
            N=int(f.readline())
            alice_list=[int(i) for i in f.readline().split(" ")]
            M=int(f.readline())
            bob_list=[int(i) for i in f.readline().split(" ")]

            i=0
            j=0
            merged_list=[]
            while i<N and j<M:
                if alice_list[i]<=bob_list[j]:
                    merged_list.append(alice_list[i])
                    i+=1
                else:
                    merged_list.append(bob_list[j])
                    j+=1
            while i<N:
                merged_list.append(alice_list[i])
                i+=1
            while j<M:
                merged_list.append(bob_list[j])
                j+=1

            merged_list_string=""
            for i in range(len(merged_list)):
                merged_list_string+=str(merged_list[i])+" "
            f1.writelines(merged_list_string)

    f.close()
    f1.close()

input_files=["input2.1.txt","input2.2.txt","input2.3.txt","input2.4.txt"]
output_files=["output2.1.txt","output2.2.txt","output2.3.txt","output2.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# This Python code reads two lists of integers from a file and merges them into a single sorted list.
# It iterates through both lists, comparing elements at each step and appending the smaller one to the merged list
# until one of the lists is exhausted. Then, it appends the remaining elements from both lists to the merged list.
# Finally, it converts the merged list to a string and writes it back to the file.