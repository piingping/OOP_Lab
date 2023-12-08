num = int(input("input: "))
if 0 <= num <10: 
    Sum = (num+((num*10)+num)+((num*100)+(num*10)+num)+((num*1000)+(num*100)+(num*10)+num))
else:
    print("error")

print(Sum)