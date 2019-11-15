a = [5, 3, 4, 2, 1]
b = [0, 1, 0, 0, 1]

d = {0:[],1:[]}
for i in range(len(a)):
    if b[i] == 0:
        d[0].append(a[i])
    elif b[i] == 1:
        d[1].append(a[i])

print(d)
    
d[0].sort(reverse=True)
d[1].sort()
print(d)
while True:
    try:
        if d[0][-1] < d[1][0]:
            d[0].remove(d[0][-1])
        if d[0][-1] > d[1][0]:
            d[1].remove(d[1][0])
    except IndexError:
        break
print(d)
if d[0] == []:
    pass
elif d[0] != []:
    print(len(d[0]))
if d[1] == []:
    pass
elif d[1] != []:
    print(len(d[1]))