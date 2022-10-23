def countingSort(a,k):
    c = [0] * (k+1)

    for j in range(len(a)):
        c[a[j]] = c[a[j]] + 1
    print(c)

    for i in range(1, k+1):
        c[i] = c[i] + c[i - 1]
    print(c)

    b = [0] * len(a)
    for j in range(len(a)-1,-1,-1):
        b[c[a[j]]-1] = a[j]
        c[a[j]] = c[a[j]] - 1
    print(b)

   
a = [3,5,1,6,7,8,3]
k=max(a)
countingSort(a,k)
