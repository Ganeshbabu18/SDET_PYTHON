# Write python code to check whether a given year is leap year or not
def is_leap_year(year):
    if year % 4 == 0:  # Leap years are divisible by 4
        if year % 100 == 0:  # Except when they are divisible by 100
            if year % 400 == 0:  # Unless they are also divisible by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# enter the year
input_year = 2024
if is_leap_year(input_year):
    print(f"{input_year} is a leap year.")
else:
    print(f"{input_year} is not a leap year.")