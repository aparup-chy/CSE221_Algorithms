
# Task 6

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        file_input = f.readlines()
        x=file_input[0]
        v1=x[0]
        y=file_input[1].split(" ")
        arr=[int(i) for i in y]
        v2=file_input[2]
        v2=int(v2[0])
        j=3
        lst=[]
        for i in range(v2):
            lst.append(file_input[j])
            j+=1
        queries=[int(i) for i in lst]

        def partition(lst,low,high):
            pivot=lst[high]
            i=low-1
            for j in range(low,high):
                if lst[j]<=pivot:
                    i+=1
                    lst[i],lst[j]=lst[j],lst[i]
            lst[i+1],lst[high]=lst[high],lst[i+1]
            return i+1

        def kth_smallest(lst,low,high,k):
            pivot_index=partition(lst,low,high)

            if pivot_index==k-1:
                return lst[pivot_index]
            elif pivot_index>k-1:
                return kth_smallest(lst,low,pivot_index-1,k)
            else:
                return kth_smallest(lst,pivot_index+1,high,k)

        def find_kth_smallest_values(lst,queries):
            result=[]
            for k in queries:
                result.append(kth_smallest(lst,0,len(lst)-1,k))
            return result

        result=find_kth_smallest_values(arr,queries)

    with open(output_file_path,"w") as f:
        for ans in result:
            f.write(str(ans)+'\n')

input_files=["input6.txt"]
output_files=["output6.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This code reads input from a file, where the first line contains information about the dataset, the second line
# contains integers to be sorted, and subsequent lines contain queries for finding the k-th smallest element. It then
# implements the quickselect algorithm to find the k-th smallest element efficiently and applies it to each query.
# The time complexity of this code is O(n+klogn), where n is the number of elements in the array and k is the number of
# queries. This complexity arises from the initial processing of the array and then performing quickselect on each query.
