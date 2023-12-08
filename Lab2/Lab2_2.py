
def count_char_in_string(x,c):
    return [ len([i[j] for j in range(len(i)) if i[j] == c]) for i in x ]
x , c = list(map(str,input().split(' '))) , str(input())
d=count_char_in_string(x,c)
print(d)



# count = 0
# for i in x:
#     for j in range(len(i)):
#         if i[j] == c:
#             count+=1
#     d.append(count)
#     count=0
# print(d)
