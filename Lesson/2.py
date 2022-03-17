count = 0
mx = 0
with open("17-1.txt", "r") as f:
    l = [int(i) for i in f]
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        if (l[i] % 160 != l[j] % 160) and ((l[i] % 7 == 0) or (l[j] % 7 == 0)):
            count += 1
            mx = max(mx, l[i] + l[j])
print(count, mx)
