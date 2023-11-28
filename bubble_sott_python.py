
list = [12, 41, 206, 48, 15, 10, 23]

n = len(list)
large = list[0]

for i in list:
    if large < i:
        large = i

print(large)
k = n
for i in range(n-1):
    for j in range(n-i-1):
        if list[j]>list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list)
