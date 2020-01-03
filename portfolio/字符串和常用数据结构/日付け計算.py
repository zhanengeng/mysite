'''入力した日付はその年何日目'''

def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year,month,day):
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_count = 0
    if leap_year(year):
        days_of_month[1] = 29

    for days in days_of_month[:month-1]:
        days_count += days
    days_count += day
    return days_count

if __name__ == "__main__":
    y = int(input("yearを入力:"))
    m = int(input("monthを入力:"))
    d = int(input("dayを入力:"))
    print(which_day(y,m,d))

    