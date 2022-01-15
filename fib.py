def f(yan):
    xan = yan*3
    xan -= 2
    fin1 = []
    tant = [0,1]
    for i in range(xan):
        shet = i
        shet2 = i+1
        newr = tant[shet] + tant[shet2]
        tant.append(int(newr))
#2part
    for i in range(xan):
        gav = tant.pop()
        if (gav % 2 == 0):
           fin1.append(gav)
    fin1.append(0)
    fin1.sort()
    fin1.count(i%2 == 0)
    return fin1

print(f(int(input())))
