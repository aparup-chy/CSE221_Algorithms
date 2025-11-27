def bubble_sort(arr):
    for i in range(len(arr)-1):
        count=0
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
        if count==0:
            return arr
    return arr

with open("input2a.txt") as f:
    n=int(f.readline())
    values=bubble_sort([int(i) for i in f.readline().split()])
    for i in range(n):
        with open("output2a.txt", "a+") as out:
            if i==0:
                out.truncate(0)
            out.write(f"{values[i]} ")

with open("input2b.txt") as f:
    n=int(f.readline())
    values=bubble_sort([int(i) for i in f.readline().split()])
    for i in range(n):
        with open("output2b.txt", "a+") as out:
            if i==0:
                out.truncate(0)
            out.write(f"{values[i]} ")

# The outer loop runs from 0 to n-2. In the best-case scenario, no swaps are needed, so the inner loop executes without
# performing any swaps. In each iteration of the outer loop, the inner loop executes len(arr) - i - 1 times, where i is
# the current iteration of the outer loop. The inner loop compares adjacent elements and swaps them if they are in the
# wrong order. In the best-case scenario, no swaps are needed, so the inner loop executes but does not perform any swaps.
# After completing the inner loop for all iterations of the outer loop, the count variable remains 0. Since the count
# remains 0 throughout, the condition if count==0: is always true, causing the function to return the sorted array immediately
# after the first iteration of the outer loop. This behavior leads to the best-case time complexity of θ(n) for the bubble
# sort algorithm, where n is the number of elements in the array.