
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        def interval(start_time,finish_time):
            idx=list(range(len(start_time)))
            idx.sort(key=lambda i: finish_time[i])
            maxt=set()
            prefint=0
            for i in idx:
                if start_time[i]>=prefint:
                    maxt.add((start_time[i],finish_time[i]))
                    prefint=finish_time[i]
            return maxt

        def schedule_remover(set):
            cst=0
            cend=0
            for i in set:
                for j in range(len(begin)):
                    if begin[j]==i[0] and cst<len(set):
                        del begin[j]
                        cst+=1
                        break
                for x in range(len(close)):
                    if close[x]==i[0] and cend<len(set):
                        del close[x]
                        cend+=1
                        break

        m,n=f.readline().split()
        m,n=int(m),int(n)
        begin=[]
        close=[]
        tcount=0
        for i in range(m):
            s1,s2=f.readline().split()
            s1,s2=int(s1),int(s2)
            begin.append(s1)
            close.append(s2)

        for i in range(n):
            tasks=interval(begin, close)
            tasks=list(tasks)
            tasks.sort(key=lambda i: i[1])
            tcount+=len(tasks)
            schedule_remover(tasks)

    with open(output_file_path,"w") as f1:
        f1.writelines(str(tcount))

input_files=["input4.1.txt","input4.2.txt","input4.3.txt","input4.4.txt","input4.5.txt"]
output_files=["output4.1.txt","output4.2.txt","output4.3.txt","output4.4.txt","output4.5.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)

# This Python code defines two functions: interval and schedule_remover.
# The interval function takes two lists representing start and finish times, sorts them based on finish times, and
# finds the maximum set of non-overlapping intervals. The schedule_remover function removes scheduled intervals from
# the begin and close lists. The main part of the code reads input, creates intervals, sorts them, counts total intervals,
# and removes scheduled intervals.