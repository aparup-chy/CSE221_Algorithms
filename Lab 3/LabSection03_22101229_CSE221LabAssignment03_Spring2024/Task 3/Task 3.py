
# Task 3

def mergesort(arr,num):
    temp_arr=[0]*num
    return invcount(arr,temp_arr,0,num-1)

def invcount(arr,temp_arr,left,right):
    count=0
    if left<right:
        mid=(left+right)//2
        count+=invcount(arr,temp_arr,left,mid)
        count+=invcount(arr,temp_arr,mid+1,right)
        count+=merge(arr,temp_arr,left,mid,right)
    return count

def merge(arr,temp_arr,left,mid,right):
    l=left
    m=mid+1
    c=left
    inv_c=0
    while l<=mid and m<=right:
        if arr[l]<=arr[m]:
            temp_arr[c]=arr[l]
            c+=1
            l+=1
        else:
            temp_arr[c]=arr[m]
            inv_c+=(mid-l+1)
            c+=1
            m+=1
    while l<=mid:
        temp_arr[c]=arr[l]
        c+=1
        l+=1
    while m<=right:
        temp_arr[c] = arr[m]
        c+=1
        m+=1

    for i in range(left,right+1):
        arr[i]=temp_arr[i]
    return inv_c

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        n=int(f.readline())
        arr=[int(i) for i in f.readline().split(" ")]

    result=mergesort(arr,n)

    with open(output_file_path,"w") as f:
        f.write(str(result).strip())

input_files=["input3.1.txt","input3.2.txt","input3.3.txt"]
output_files=["output3.1.txt","output3.2.txt","output3.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# This code implements an inversion count algorithm using merge sort to find the number of inversions in an array.
# It counts the number of times elements are out of order and returns the count. The time complexity of this code is
# O(nlogn), where n is the number of elements in the input array, due to the merge sort algorithm.
