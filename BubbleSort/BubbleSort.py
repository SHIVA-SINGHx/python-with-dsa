def bubbleSort(a):
    n = len(a)
    
    for i in range(n): ## outer loop
        for j in range(0, n-1-i): ## inner loop
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]  ## swipe the value
                

a = [64, 45, 7834, 33, 1, 7 ]
bubbleSort(a)
print(a)
        