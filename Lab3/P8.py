from datetime import datetime

dt = datetime.now()
print(dt)


get_an   = lambda d: d.strftime("%Y")
get_luna = lambda d: d.strftime("%m")
get_zi   = lambda d: d.strftime("%d")
get_ora  = lambda d: d.strftime("%H:%M:%S.%f")

print(get_an(dt))
print(get_luna(dt))
print(get_zi(dt))
print(get_ora(dt))