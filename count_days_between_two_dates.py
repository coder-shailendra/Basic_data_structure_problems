from datetime import datetime

def days_between(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

date1 = "2026-05-12"
date2 = "2025-12-24"

print(days_between(date1, date2))
