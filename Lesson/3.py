count = 0
mx = 0
with open("17-2.txt", "r") as f:
    a = [int(i) for i in f]
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if ((a[i] - a[j]) % 2 == 0) and ((a[i] % 31 == 0) or (a[j] % 31 == 0)):
            count += 1
            mx = max(mx, a[i] + a[j])
print(count, mx)
