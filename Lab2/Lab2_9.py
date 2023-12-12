month = [0,1,2,3,4,5,6,7,8,9,10,11,12]

def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year%100 != 0) :
        return True
    else: 
        return False

def days_of_year(day, month, year):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    leap_check = is_leap(year)
    if leap_check:
        days[2] = 29
    for i in range(1,len(days)):
         days[i]+=days[i-1]
    if not (1 <= month <= 12):
        return -1
    if not (1 <= day <= days[month] ):
        return -1
    return days[month-1] + day

def days_in_year(year):
    leap_check = is_leap(year)
    if leap_check:
        return 366
    else: return 365,

def date_diff(start, stop):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    year_diff = stop[2]-start[2]
    date_diff = 0
    if year_diff > 1:
        date_diff = days_left_in_start_year + number_of_days_2+1
        for i in range (start+1, stop, +1):
            leap_check = is_leap(i)
            if leap_check:
                 date_diff += 366
            else: date_diff += 365
    else: 
         date_diff = days_of_year(stop[0],stop[1], stop[2])-days_of_year(start[0], start[1], start[2])

#  only leap year that has 29 days in Feb. if False, return -1
    if start[1] == 2:
        if not (1 <= start[0] <= 29 if is_leap(start[2]) else 1 <= start[0] <= 28):
            return -1
    if stop[1] == 2:
        if not (1 <= stop[0] <= 29 if is_leap(stop[2]) else 1 <= stop[0] <= 28):
            return -1
        
#     เช็คว่าเดือนต้องอยู่ระหว่าง 1-12
    if not (1 <= start[1] <= 12 and 1 <= stop[1] <= 12):
        return -1


#     วันที่ถูกต้อง
    if start[0] > days[start[1]] or stop[0] > days[stop[1]]:
        return -1
    
    return date_diff

list_of_dates=[]
for i in range(0,2):
    input_date = list(map(int,input().split("-")))
    list_of_dates.append(input_date)


numbers_in_year_1 = days_in_year(list_of_dates[0][2])

res=""
for i in numbers_in_year_1:
    res+=str(i)
res=int(res)

days_of_year_1 = days_of_year(list_of_dates[0][0], list_of_dates[0][1], list_of_dates[0][2])
days_left_in_start_year =  res - days_of_year_1 


number_of_days_2 = days_of_year(list_of_dates[1][0], list_of_dates[1][1], list_of_dates[1][2])

ans=date_diff(list_of_dates[0], list_of_dates[1])
print(days_left_in_start_year, number_of_days_2)

print(ans)
