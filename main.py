
f = open("/Users/yaroslavmartynenko/Downloads/1.txt", "rt")
a=int(input("Введіть певне значення у форматі AAA"))
for i in f:
    x = i.find(" ")
    x += 1
    y = ''
    for j in range(x, len(i)-1):
        y += i[j]
    y = int(y)
    if y > a:
        print(i[0:x])