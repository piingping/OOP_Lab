def count_minus(c):
    return len([i for i in c if i < 0])

x = list(map(int,input().split(' ')))
print(count_minus(x))