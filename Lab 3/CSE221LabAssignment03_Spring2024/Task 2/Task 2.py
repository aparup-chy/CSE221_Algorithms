
# Task 2

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        x=int(f.readline())
        arr=[int(i) for i in f.readline().split(" ")]

        def find_max(arr,low,high):
            if low==high:
                return arr[low]
            mid=(low+high)//2
            left_max=find_max(arr,low,mid)
            right_max=find_max(arr,mid+1,high)
            return max(left_max,right_max)

    with open(output_file_path,"w") as f1:
        max_value = find_max(arr,0,x-1)
        f1.writelines(str(max_value))

    f.close()
    f1.close()

input_files=["input2.1.txt","input2.2.txt","input2.3.txt","input2.4.txt"]
output_files=["output2.1.txt","output2.2.txt","output2.3.txt","output2.4.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# This code reads integers from an input file, finds the maximum value using a recursive divide-and-conquer approach,
# and writes the maximum value into an output file. The find_max function recursively divides the array into halves
# until it reaches individual elements, then compares and returns the maximum value. The time complexity of this code
# is O(n) due to the recursive calls, where n is the number of integers in the input array. The space complexity is
# O(logn) due to the recursive call stack.
