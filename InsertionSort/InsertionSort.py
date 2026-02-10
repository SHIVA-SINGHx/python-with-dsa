def InsertionSort(a):
    n = len(a) # length of the array or list
    
    for i in range(1, n):
        key = a[i] # This is the key variable
        j = i - 1 
        while ( j >= 0 and key < a[j]):
            a[j+1] = a[j]
            j = j-1 
            
        a[j+1] = key
        
        
a = [64, 56, 42, 56, 77, 245, 567,12,8]
InsertionSort(a)
print(a)