
def selection_sort(arr,arr2):
    for i in range(len(arr)):
        idx=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[idx]:
                idx=j
            elif arr[j]==arr[idx]:
                if arr2[j]<arr2[idx]:
                    idx=j
        arr[idx],arr[i]=arr[i],arr[idx]
        arr2[idx],arr2[i]=arr2[i],arr2[idx]
    return arr,arr2

with open("input3a.txt") as f:
    n=int(f.readline())
    ids=[int(i) for i in f.readline().split()]
    marks=[int(i) for i in f.readline().split()]
    marks,ids=selection_sort(marks,ids)
    for i in range(n):
        with open("output3a.txt","a+")as out:
            if i == 0:
                out.truncate(0)
            out.write(f"ID: {ids[i]} Mark: {marks[i]}\n")

with open("input3b.txt") as f:
    n=int(f.readline())
    ids=[int(i) for i in f.readline().split()]
    marks=[int(i) for i in f.readline().split()]
    marks,ids=selection_sort(marks,ids)
    for i in range(n):
        with open("output3b.txt","a+") as out:
            if i==0:
                out.truncate(0)
            out.write(f"ID: {ids[i]} Mark: {marks[i]}\n")