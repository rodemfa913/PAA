a = []

def divideAndConquer(left, right):
    # condição de parada: um único elemento
    if left == right:
        if a[left] > 0:
            return a[left]
        else:
            return 0
    else:
        mid = (left + right) // 2
        
        # soma parte esquerda
        maxLeft = 0
        summ = 0
        for k in range(mid, left - 1, -1):
            summ += a[k]
            if summ > maxLeft:
                maxLeft = summ
        
        # soma parte direita
        maxRight = 0
        summ = 0
        for k in range(mid + 1, right + 1):
            summ += a[k]
            if summ > maxRight:
                maxRight = summ
        
        return max(max(divideAndConquer(left, mid), divideAndConquer(mid + 1, right)), maxLeft + maxRight)

while True:
    n = int(input())
    if n <= 0:
        break
    a.clear()
    for i in range(n):
        a.append(int(input()))
    print(divideAndConquer(0, n - 1))
