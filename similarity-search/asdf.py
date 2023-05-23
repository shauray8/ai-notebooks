n = int(input())
a = list(map(int, input().split()))
ans = n
for i in range(n - 1):
    if (a[i] + 1) % a[i + 1] == 0 or (a[i + 1] + 1) % a[i] == 0:
        ans = min(ans, n - 2)
    else:
        ans = min(ans, n - 1)
print(ans)
