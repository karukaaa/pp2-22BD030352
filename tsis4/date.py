import datetime as dt

today = dt.datetime.now()
some_date = dt.datetime.strptime('2023-02-21 13-10-10', '%Y-%m-%d %H-%M-%S')


def five_days():
    return "5 days ago: ", dt.date.today()-dt.timedelta(5)


def yesterday_tomorrow():
    print("Yesterday: ", dt.date.today()-dt.timedelta(days=1))
    print("Today: ", dt.date.today())
    print("Tomorrow: ", dt.date.today() + dt.timedelta(days=1))


def drop_microseconds():
    return dt.datetime.today().replace(microsecond=0)


def dif_seconds(date1, date2):
    dt.timedelta = date2 - date1
    return dt.timedelta.days*24*3600 + dt.timedelta.seconds


