
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        def interval(start_time, finish_time):
            idx=list(range(len(start_time)))
            idx.sort(key=lambda i: finish_time[i])
            dset=set()
            prev_finish_time=0
            for i in idx:
                if start_time[i]>=prev_finish_time:
                    dset.add((start_time[i],finish_time[i]))
                    prev_finish_time=finish_time[i]
            return dset

        s=f.readline()
        s=int(s)
        initial=[]
        finish=[]

        for i in range(s):
            s1,s2=f.readline().split()
            s1,s2=int(s1),int(s2)
            initial.append(s1)
            finish.append(s2)

    with open(output_file_path,"w") as f1:
        tasks=interval(initial, finish)
        tasks=list(tasks)
        tasks.sort(key=lambda i: i[1])
        f1.writelines(f'{len(tasks)}\n')
        for i in tasks:
            for j in i:
                f1.writelines(f'{j} ')
            f1.writelines(f'\n')

input_files=["input3.1.txt","input3.2.txt","input3.3.txt"]
output_files=["output3.1.txt","output3.2.txt","output3.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This Python code reads input from a file, where each line represents a start and finish time pair.
# It defines a function interval to find non-overlapping intervals, sorts them based on finish times, and
# writes them to an output file along with their count. Finally, it writes the sorted intervals to the output file
# with each interval on a new line and the count of intervals on the first line.