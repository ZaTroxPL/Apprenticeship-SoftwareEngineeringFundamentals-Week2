from datetime import datetime
import calendar

#date = input("insert date (format: DD/MM/YYYY): ")

print(calendar.day_name[datetime.now().weekday()])