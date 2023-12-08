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

def days_in_year(year):
    leap_check = is_leap(year)
    if leap_check==True:
        return 366
    else: return 365

def date_diff(start, stop):
    year_diff = stop-start
    date_diff = days_left_in_start_year+number_of_days_2
    if year_diff != 0:
        for i in range (start+1, stop, +1):
            leap_check = is_leap(i)
            if leap_check==True:
                 date_diff += 366
            else: date_diff += 365

    return date_diff


list_of_dates=[]
for i in range(0,2):
    input_date = list(map(int,input().split(' ')))
    list_of_dates.append(input_date)

numbers_in_year_1 = days_in_year(list_of_dates[0][2])
days_of_year_1 = days_of_year(list_of_dates[0][0], list_of_dates[0][1], list_of_dates[0][2])
days_left_in_start_year =  numbers_in_year_1 - days_of_year_1 

number_of_days_2 = days_in_year(list_of_dates[1][2])

ans=date_diff(list_of_dates[0][2], list_of_dates[1][2])
print(ans)
    