def add2list(lst1, lst2):
    return [lst1[i] + lst2[i] for i in range(len(lst1))]

x = [1, 3, 4]
y = [2, 7, 6]

print(add2list(x, y))
