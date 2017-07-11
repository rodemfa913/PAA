while True:
    n = int(input())
    if n <= 0:
        break
    
    maxSum = 0
    begin = end = -1
    a = []
    
    for i in range(n):
        a.append(int(input())
    
    for first in range(n):
        for last in range(first, n):
            summ = 0
            for k in range(first, last + 1):
                summ += a[k]
            
            if summ > maxSum:
                maxSum = summ
                begin = first
                end = last
    
    print("{0} {1} {2}".format(maxSum, begin, end))
