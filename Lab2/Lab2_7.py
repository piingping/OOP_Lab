days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year%100 != 0) :
        return True
    else: False

def days_of_year(day, month, year):
    leap_check = is_leap(year)
    if leap_check == True:
        days[1] = 29
    for i in range(1,len(days)):
         days[i]+=days[i-1]
    return days[month-1] + day
    
input_date = list(map(int,input().split(' ')))
leap_check = is_leap(input_date[2])
number_of_days = days_of_year(input_date[0], input_date[1], input_date[2])

print(leap_check, number_of_days)