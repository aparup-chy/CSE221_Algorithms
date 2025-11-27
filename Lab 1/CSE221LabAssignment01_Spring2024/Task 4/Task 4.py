
def sort(arr,arr2):
    for i in range(len(arr)-1):
        count=0
        for j in range(len(arr)-i-1):
            if arr[j].split()[0]>arr[j+1].split()[0]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
        count+=1
        if count==0:
            break
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j].split()[0]==arr[j+1].split()[0]:
                if int(arr2[j][-6:].replace(":",""))<int(arr2[j+1][-6:].replace(":","")):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
    return arr,arr2

with open("input4.txt") as f:
    n=int(f.readline())
    texts,times=[],[]
    for i in range(n):
        line=f.readline()
        texts.append(line[:-6]),times.append(line[-6:])
    texts,times=sort(texts,times)
    for i in range(n):
        with open("output4.txt","a+") as out:
            if i==0:
                out.truncate(0)
            out.write(f"{texts[i]}{times[i]}")
