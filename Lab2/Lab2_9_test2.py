days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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
    if not (1 <= month <= 12):
        raise ValueError("Invalid month. Month should be between 1 and 12.")
    if not (1 <= day <= days[month] - days[month - 1]):
        raise ValueError("Invalid day for the given month")
    return days[month - 1] + day

def days_in_year(year):
    leap_check = is_leap(year)
    if leap_check:
        return 366
    else:
        return 365

def date_diff(start, stop):
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

    # Check for errors and raise ValueError if conditions are not met
    if list_of_dates[0][1] == 2:
        max_days_in_feb = 29 if is_leap(list_of_dates[0][2]) else 28
        if not (1 <= list_of_dates[0][0] <= max_days_in_feb):
            raise ValueError(f"Invalid day for February in the first date. Should be between 1 and {max_days_in_feb}")

    if list_of_dates[1][1] == 2:
        max_days_in_feb = 29 if is_leap(list_of_dates[1][2]) else 28
        if not (1 <= list_of_dates[1][0] <= max_days_in_feb):
            raise ValueError(f"Invalid day for February in the second date. Should be between 1 and {max_days_in_feb}")

    if not (1 <= list_of_dates[0][1] <= 12 and 1 <= list_of_dates[1][1] <= 12):
        raise ValueError("Invalid month. Month should be between 1 and 12.")

    if list_of_dates[0][0] > days[list_of_dates[0][1]] or list_of_dates[1][0] > days[list_of_dates[1][1]]:
        raise ValueError("Invalid day for the given month")

    # ... (rest of the code)

# Input dates
list_of_dates = []
for i in range(2):
    input_date = list(map(int, input().split("-")))
    list_of_dates.append(input_date)

# Calculate days_left_in_start_year and number_of_days_2
days_in_year_1 = days_in_year(list_of_dates[0][2])
days_of_year_1 = days_of_year(list_of_dates[0][0], list_of_dates[0][1], list_of_dates[0][2])
days_left_in_start_year = days_in_year_1 - days_of_year_1

number_of_days_2 = days_of_year(list_of_dates[1][0], list_of_dates[1][1], list_of_dates[1][2])

# Calculate date difference
ans = date_diff(list_of_dates[0][2], list_of_dates[1][2])
print(ans)
