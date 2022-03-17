mxsum = 0
count = 0
with open("17.txt", "r") as f:
    l = f.readlines()
    for i in range(len(l)-1):
        if (int(l[i]) % 3 == 0) or (int(l[i+1]) % 3 == 0):
            count += 1
            mxsum = max(mxsum, int(l[i]) + int(l[i+1]))
print(count, mxsum)
