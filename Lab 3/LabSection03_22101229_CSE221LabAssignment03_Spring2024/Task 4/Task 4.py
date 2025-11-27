
# Task 4

def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        n=int(f.readline())
        arr=[int(i) for i in f.readline().split(" ")]

    newarr=[]
    for i in arr:
        newarr.append(int(i))
    def mul(newarr):
        mid=len(newarr)//2
        m1=max(newarr[:mid])
        m2=max([abs(i) for i in newarr[mid:]])
        return m1+m2**2
    def maxf(newarr):
        if len(newarr)==1:
            return float("-inf")
        if len(newarr)==2:
            return newarr[0]+newarr[1]**2
        m1=maxf(newarr[:len(newarr)//2])
        m2=maxf(newarr[len(newarr)//2:])
        multiply_max=mul(newarr)
        return max(m1,m2,multiply_max)


    p=maxf(newarr)

    with open(output_file_path,"w") as f:
        f.write(str(p))

input_files=["input4.1.txt","input4.2.txt","input4.3.txt"]
output_files=["output4.1.txt","output4.2.txt","output4.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

#  This code reads integers from an input file, processes them, and finds the maximum value based on a specific formula,
#  then writes it into an output file. The maxf function recursively divides the array, finds the maximum values, and
#  calculates a maximum based on certain conditions. The time complexity of this code is O(nlogn) due to the recursion
#  in the maxf function, where n is the number of elements in the input array.
