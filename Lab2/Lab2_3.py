def delete_minus(x):
    return [ [i[j] for j in range(len(i)) if i[j] > 0] for i in x ]

x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ] 
print(delete_minus(x))