n = int(input())
if n == 1:
    print([[1]])
else:
    L = [[1],[1,1]]
    for i in range(n-2):
        L.append([1])
        for j in range(len(L[-2])-1):
            L[-1].append(L[-2][j]+L[-2][j+1])
        L[-1].append(1)
    print(L)
