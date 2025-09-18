#Start datum ex 2025-09-01
#Slut datum ex 2025-10-01
#Elmätarens värde vid start datum ex 1532
#Elmätarens värde vid slut datum ex 2421
#Dagsavgift ex 5kr
#Kwh pris ex 0.76kr
import datetime
year = int(input('enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date1 = datetime.date(year, month, day)
print(date1)
year2 = int(input('enter a year'))
month2 = int(input('Enter a month'))
day2 = int(input('Enter a day'))
date2 = datetime.date(year2, month2, day2)
print(date2)
print(date2 - date1)
meterstart = int(input('meterstart'))
meterend = int(input('meterend'))
consumed = meterend - meterstart
fee = int(input('fee'))
kwh = int(input('kw/h'))
date_diff = (date2 - date1).days
print((date_diff * fee + kwh * consumed) * 1.25)