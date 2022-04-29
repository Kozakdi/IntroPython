import datetime

print(datetime.date(2021, 1, 1))
print(datetime.date.today())
print(datetime.time(12, 46, 30))

print(datetime.datetime.now())
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())


print(datetime.timedelta(days=7))
delta = datetime.timedelta(days=7)
now = (datetime.datetime.now())

print(now - delta)

now = (datetime.datetime.now())
date = datetime.datetime(2022, 1, 1)
print(now - date)

now = (datetime.datetime.now())
date = datetime.datetime(2022, 1, 1)
delta = now - date
print(delta.days, 'days')
