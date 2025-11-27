
f=open("C:/Users/ASUS/PycharmProjects/CSE221 (MTD)/Lab 1/Task 1/Task 1a/input1a.txt","r")
f1=open("C:/Users/ASUS/PycharmProjects/CSE221 (MTD)/Lab 1/Task 1/Task 1a/output1a.txt","w")

s=f.readline()
for lines in f:
    n=int(lines)
    if n%2==0:
        f1.writelines(str(n)+" is an Even number.\n")
    else:
        f1.writelines(str(n)+" is an Odd number.\n")

f.close()
f1.close()
