# Using O(NlogN) Complexity

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        with open(output_file_path,"w") as f1:
            f.readline()
            alice_list=[int(i) for i in f.readline().split(" ")]
            f.readline()
            bob_list=[int(i) for i in f.readline().split(" ")]

            def merge_sort_merge(alice_list, bob_list):
                merged_list=[]
                i=0
                j=0
                while i<len(alice_list) and j<len(bob_list):
                    if alice_list[i]<=bob_list[j]:
                        merged_list.append(alice_list[i])
                        i+=1
                    else:
                        merged_list.append(bob_list[j])
                        j+=1
                while i<len(alice_list):
                    merged_list.append(alice_list[i])
                    i+=1
                while j<len(bob_list):
                    merged_list.append(bob_list[j])
                    j+=1
                return merged_list

            def merge_sort(arr):
                if len(arr)<=1:
                    return arr
                mid=len(arr) // 2
                left=merge_sort(arr[:mid])
                right=merge_sort(arr[mid:])
                return merge_sort_merge(left,right)

            merged_list=merge_sort_merge(alice_list, bob_list)
            sorted_list=merge_sort(merged_list)
            sorted_list_string=""
            for i in range(len(sorted_list)):
                sorted_list_string+=str(sorted_list[i])+" "
            f1.writelines(sorted_list_string)

    f.close()
    f1.close()

input_files=["input2.1.txt","input2.2.txt","input2.3.txt","input2.4.txt"]
output_files=["output2.1.txt","output2.2.txt","output2.3.txt","output2.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This Python code reads two lists of integers from a file, then defines two functions: merge_sort_merge to
# merge two sorted lists and merge_sort to recursively sort a list using merge sort algorithm. It applies the
# merge_sort_merge function to merge Alice's and Bob's lists, then sorts the merged list using merge_sort.
# Finally, it converts the sorted list to a string and writes it back to the file.