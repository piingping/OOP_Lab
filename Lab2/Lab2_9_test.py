
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def days_of_year(day, month, year):
    leap_check = is_leap(year)
    if leap_check:
        days[2] = 29
    for i in range(1, len(days)):
        days[i] += days[i - 1]
    if list_of_dates[0][1] > 12 or list_of_dates[1][1] > 12:
        return -1
    return days[month - 1] + day

def days_in_year(year):
    leap_check = is_leap(year)
    if leap_check:
        return 366
    else:
        return 365

def date_diff(start, stop):
    # Validate input dates
    if not (1 <= list_of_dates[0][1] <= 12 and 1 <= list_of_dates[1][1] <= 12):
        return -1

    if not (1 <= list_of_dates[0][0] <= days[list_of_dates[0][1]] and 1 <= list_of_dates[1][0] <= days[list_of_dates[1][1]]):
        return -1

    if list_of_dates[0][1] == 2:
        if not (1 <= list_of_dates[0][0] <= 29 if is_leap(list_of_dates[0][2]) else 1 <= list_of_dates[0][0] <= 28):
            return -1

    if list_of_dates[1][1] == 2:
        if not (1 <= list_of_dates[1][0] <= 29 if is_leap(list_of_dates[1][2]) else 1 <= list_of_dates[1][0] <= 28):
            return -1
        
    # if list_of_dates[0][1] > 12 or list_of_dates[1][1] > 12:
    #     return -1
    
    year_diff = stop-start
    date_diff = days_left_in_start_year + number_of_days_2+1
    if year_diff > 1:
        for i in range (start+1, stop, +1):
            leap_check = is_leap(i)
            if leap_check:
                 date_diff += 366
            else: date_diff += 365
    else: 
        pass

    

    return date_diff

list_of_dates = []
for i in range(0, 2):
    input_date = list(map(int, input().split("-")))
    list_of_dates.append(input_date)

# Calculate the number of days in the start and stop years
days_in_year_1 = days_in_year(list_of_dates[0][2])
days_of_year_1 = days_of_year(list_of_dates[0][0], list_of_dates[0][1], list_of_dates[0][2])
days_left_in_start_year = days_in_year_1 - days_of_year_1

number_of_days_2 = days_of_year(list_of_dates[1][0], list_of_dates[1][1], list_of_dates[1][2])

# Calculate the date difference
ans = date_diff(list_of_dates[0][2], list_of_dates[1][2])

# Print the result
print(ans)

    
