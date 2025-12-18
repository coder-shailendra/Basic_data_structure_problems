from datetime import date

def day_of_week(day, month, year):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    
    return days[date(year, month, day).weekday()]

print(day_of_week(12,12,2025))
print(day_of_week(12,5,2026))