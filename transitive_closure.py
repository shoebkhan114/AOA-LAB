matrix = []
n = int(input("Enter NO. of Node:- "));
for i in range(n):
    ls = list(map(int,input().split()))
    matrix.append(ls)
for k in range(n):
    for i in range(n):
        for j in range(n):
           matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

print("--------Transitive Closure----------")
for i in matrix:
    print(i)
        
