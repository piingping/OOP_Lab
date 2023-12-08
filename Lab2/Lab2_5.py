def only_english(string1):
    return "".join([i for i in string1 if i.isupper()==True or i.islower()==True])

x = input()
print(only_english(x))