in_h, in_min, out_h, out_min = map(int, input().split())
money = 0
time_diff = (out_h * 60 + out_min) - (in_h * 60 + in_min)

# if out_h > 23 or in_h <= 6 or out_min>=60 or in_min>= 60 or in_h > out_h or time_diff > 960 :
#   print("Error")
#   exit()

# if out_h == 23 and out_min > 0:
#   print("Error")
#   exit()

# elif in_h==out_h and out_min<in_min:
#   print("Error")
#   exit()

if (out_h * 60 + out_min) > 23*60 or (in_h * 60 + in_min) < 7*60:
  print("Error")
  exit()
  
elif time_diff <= 15:
  money += 0

elif time_diff <= 180 and time_diff>15:
    money += 10 * (((time_diff-1) // 60)) + 10

elif time_diff>180 and time_diff <= 360:
    money += 10 * (((time_diff)//60)) + 20
    if time_diff%60 > 0 and time_diff>240:
        money += 10
    
elif time_diff > 360:
    money = 200

print(money)