orig_list = list(map(int,input().split(' ')))
result = sorted([i for i in orig_list])

temp=result.count(0)
for i in range(len(result)):
    if i < temp:
        result.pop(0)
        
ans = result.copy()
if(temp>0):
    for i in range(len(result)):
        if (result[i]>ans[0]):
            for j in range(temp):
                ans.insert(i,0)
                temp-=1
ans = list(map(str,ans))   

print("".join(ans))

