string = input()
String_num = len(string)
lower, upper = 0,0
for i in range (String_num):
    if string[i].isupper()==True:
        upper+=1
    else:
        lower+=1
print(lower)
print(upper)
