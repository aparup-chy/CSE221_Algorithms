
# Task 5

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        n=int(f.readline())
        arr=[int(i) for i in f.readline().split(" ")]
        narr=[]
        for i in arr:
            narr.append(int(i))

        def quick_sort(narr,p,r):
            if p<r:
                q=partn(narr,p,r)
                quick_sort(narr,p,q-1)
                quick_sort(narr,q+1,r)

        def partn(narr, p, r):
            pivot=narr[p]
            left=p+1
            right=r
            while True:
                while left<=right and narr[left]<=narr[p]:
                    left=left + 1
                while left<=right and narr[right]>=narr[p]:
                    right=right-1
                if right<left:
                    break
                else:
                    narr[left],narr[right]=narr[right],narr[left]
            narr[p],narr[right]=narr[right],narr[p]
            return right

        m=len(narr)-1
        quick_sort(narr,0,m)
        k=''
        for i in narr:
            k=k+" "+str(i)

    with open(output_file_path,"w") as f:
        f.write(str(k).strip())

input_files=["input5.1.txt","input5.2.txt","input5.3.txt","input5.4.txt"]
output_files=["output5.1.txt","output5.2.txt","output5.3.txt","output5.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This code reads integers from an input file, performs in-place quicksort on the array, and writes the sorted integers
# into an output file. The quick_sort function recursively partitions the array based on a pivot element, while partn function
# assists in the partitioning process. The time complexity of this code is O(nlogn) in the average case and O(n^2) in
# the worst case, where n is the number of elements in the input array.