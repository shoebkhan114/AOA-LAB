n = int(input("Enter number of Item: "))
W = int(input("Enter Max Capecity of Weight: "))
wt = []
val = []
for i in range(n):
    w = int(input(f"Enter Weight of {i+1}: "))
    wt.append(w)
print("---------------------")    
for i in range(n):
    v = int(input(f"Enter Profit on {i+1}: "))
    val.append(v)
dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
for i in range(n+1):
    for w in range(W+1):
        if i == 0 or w == 0:
            dp[i][w] = 0
        elif wt[i-1] <= w:
            dp[i][w] = max(dp[i - 1][w],val[i - 1] + dp[i - 1][w - wt[i - 1]])
        else:
            dp[i][w] = dp[i - 1][w]

solution = [0] * n
i = n
w = W

while i > 0 and w > 0:

    # Item selected
    if dp[i][w] != dp[i - 1][w]:
        solution[i - 1] = 1
        w -= wt[i - 1]

    i -= 1

print("\nMaximum Profit =", dp[n][W])  
print("Solution Vector =", solution)          
