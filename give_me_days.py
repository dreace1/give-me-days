import calendar
import sys

def get_month_days(year: int, month: int) -> list:
    cal = calendar.monthcalendar(year, month)
    month_days = []
    german_weekdays = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']


    for week in cal:
        for day in week:
            if day != 0:
                weekday_number = calendar.weekday(year, month, day)
                weekday_name = german_weekdays[weekday_number]
                month_days.append(f"{day}. {weekday_name}")

    return month_days

if __name__ == "__main__":
    if len(sys.argv) > 1:
        days_of_month = get_month_days(int(sys.argv[1]), int(sys.argv[2]))
        for day in days_of_month:
            print(day)
    else:
        print("Bitte Jahr und Monat als int angeben")

    
    