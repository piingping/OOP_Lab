last_i = 0
last_j = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        str_num = str(num)
        if str_num == str_num[::-1]:
            last_i = i
            last_j = j

print(last_i, '*', last_j)
