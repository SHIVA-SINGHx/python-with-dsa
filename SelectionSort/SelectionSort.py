def SelectionSort(a):
    n = len(a)
    
    for i in range(n):
        min = i
        for j in range(i, n):
            if(a[min] > a[j]):
                min = j
                
        a[i], a[min] = a[min], a[i]
        

a = [64, 55, 56,76, 787, 89,45, 15, 2, 3, 4,]
SelectionSort(a)
print(a)
        
            