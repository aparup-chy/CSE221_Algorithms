
f=open("C:/Users/ASUS/PycharmProjects/CSE221 (MTD)/Lab 1/Task 1/Task 1b/input1b.txt","r")
f1=open("C:/Users/ASUS/PycharmProjects/CSE221 (MTD)/Lab 1/Task 1/Task 1b/output1b.txt","w")

s=f.readline()
for i in range(int(s)):
    lines=f.readline()
    vals=lines.strip("\n").split(" ")
    if vals[2]=="+":
        add=int(vals[1])+int(vals[3])
        f1.write("The result of "+vals[1]+" + "+vals[3]+" is "+str(add)+"\n")
    elif vals[2]=="-":
        sub=int(vals[1])-int(vals[3])
        f1.write("The result of " + vals[1] + " - " + vals[3] + " is " + str(sub)+"\n")
    elif vals[2]=="*":
        mul=int(vals[1])*int(vals[3])
        f1.write("The result of " + vals[1] + " * " + vals[3] + " is " + str(mul)+"\n")
    elif vals[2]=="/":
        div=int(vals[1])/int(vals[3])
        f1.write("The result of " + vals[1] + " / " + vals[3] + " is " + str(div)+"\n")

f.close()
f1.close()

