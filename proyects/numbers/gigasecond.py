from datetime import datetime, timedelta
def add(moment):
    days = int(10**9/86400)
    hours = int((10**9 % 86400) / 3600)
    minutes = int(((10**9 % 86400) % 3600) / 60)
    seconds = int(((10**9 % 86400) % 3600) % 60)
    time_delta = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
  #  print(time_delta)
  #  print(timedelta(seconds=10**9))
  #  return (moment + timedelta(seconds=10**9))
    return (moment+time_delta)

#se debe convertir los segundos o el gigasegundo 10^9 en una fecha y eso hacer timedelta y lo suma
#a otra fecha en formato datetime.

a = add(datetime(2015, 1, 24, 23, 59, 59))
print(a)