import datetime


# Timezone
# Make a date, time, or datetime object "aware"
timezoneCst = datetime.timezone(-datetime.timedelta(hours=6))  # UTC-6 -- note the negative in "-datetime.timedelta(...)"

naiveDatetime = datetime.datetime.now()  # "naive"
awareDatetime = datetime.datetime.now(timezoneCst)


print("naive datetime:", naiveDatetime)
print("aware datetime:", awareDatetime)

# 1 day ahead of today
print("1 day ahead:", datetime.datetime.now() + datetime.timedelta(days=1))

# current time in UTC timezone
print("current datetime in UTC timezone:", datetime.datetime.now(datetime.timezone.utc))

# make datetime object from timestamp string
print("datetime made from string:", datetime.datetime.fromisoformat("2024-09-22 16:45:13.180946-06:00"))
print()

# strftime()
# format a datetime (or date/time) object into an explicit string format
formattedDatetime = awareDatetime.strftime("%B %d, %Y - %H%M%z")  # 24-hour
print(formattedDatetime)
formattedDatetime = awareDatetime.strftime("%B %d, %Y - %I:%M %p UTC%z")  # 12-hour
print(formattedDatetime)
print()

# make naive datetime aware (give the Datetime a timezone, so doesn't change time)
print("making datetimes aware")
madeAwareDatetime = naiveDatetime.replace(tzinfo=timezoneCst)
print("naive datetime given a timezone and made aware:", madeAwareDatetime)
print()

# convert aware datetime from one timezone to another
currentUtcDatetime = datetime.datetime.now(datetime.timezone.utc)
print("current time in UTC:", currentUtcDatetime)
currentCSTDatetime = currentUtcDatetime.astimezone(timezoneCst)
print("current time in CST:", currentCSTDatetime)

# converting naive datetimes to different timezones is also possible (just assumes naive is in local timezone)
convertedFromNaive = naiveDatetime.astimezone(datetime.timezone.utc)
print("also works with naive datetimes, just assumes it is in system's local timezone:", convertedFromNaive)
print()

# get difference in days between 2 dates
currentTime = datetime.datetime.now()
currentTimePlus23 = currentTime + datetime.timedelta(hours=23)
currentTimePlus24 = currentTime + datetime.timedelta(hours=24)
withHoursRemaining = (currentTimePlus23 - currentTime).days
withDayRemaining = (currentTimePlus24 - currentTime).days
print("hours minutes and seconds:", currentTime.time())
print("just the date:", currentTime.date())
print("with less than 1 day remaining:", withHoursRemaining)
print("with exactly 1 day remaining:", withDayRemaining)
print()