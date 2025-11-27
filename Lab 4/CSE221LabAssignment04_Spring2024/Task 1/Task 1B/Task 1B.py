
def run_code(input_file_path,output_file_path):
    with open(input_file_path,"r") as f:
        n,m=[int(i) for i in f.readline().split()]
        d_dict={}
        for i in range(n+1):
            d_dict.update({i:[]})
        for j in range(m):
            x=f.readline().split()
            a,b,c=x
            d_dict[int(a)].append((int(b),int(c)))

    with open(output_file_path, "w") as f1:
        for k in d_dict.keys():
            f1.write(f'{k} : ')
            for x in d_dict[k]:
                f1.write(str(x)+" ")
            f1.write("\n")
        f.close()
        f1.close()

input_files=["input1B.1.txt","input1B.2.txt","input1B.3.txt"]
output_files=["output1B.1.txt","output1B.2.txt","output1B.3.txt"]

for i in range(len(input_files)):
    input_file=input_files[i]
    output_file=output_files[i]
    run_code(input_file,output_file)


# Created dictionary for performing an adjacency list.
