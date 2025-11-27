
# Task 1

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        x=int(f.readline())
        arr=[int(i) for i in f.readline().split(" ")]

        def merge(a,b):
            merged=[]
            i=0
            j=0

            while i<len(a) and j<len(b):
                if a[i]<=b[j]:
                    merged.append(a[i])
                    i+=1
                else:
                    merged.append(b[j])
                    j+=1

            while i<len(a):
                merged.append(a[i])
                i+=1

            while j<len(b):
                merged.append(b[j])
                j+=1

            return merged

        def mergeSort(arr):
            if len(arr)<=1:
                return arr
            else:
                mid=len(arr)//2
                a1=mergeSort(arr[:mid])
                a2=mergeSort(arr[mid:])
                return merge(a1,a2)

        sorted_list=mergeSort(arr)
        sorted_list_string=""
        for i in range(len(sorted_list)):
            sorted_list_string+=str(sorted_list[i])+" "

    with open(output_file_path,"w") as f1:
        f1.writelines(sorted_list_string)

    f.close()
    f1.close()

input_files=["input1.1.txt","input1.2.txt","input1.3.txt","input1.4.txt"]
output_files=["output1.1.txt","output1.2.txt","output1.3.txt","output1.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This code reads integers from an input file, sorts them using merge sort, and writes the sorted integers into
# an output file. It defines functions for merge sort and merging arrays, reads input from a file, sorts it, and
# writes the sorted output to another file. The time complexity of this code is O(nlogn).
