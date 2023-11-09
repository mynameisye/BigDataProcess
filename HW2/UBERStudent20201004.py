import sys
import calendar


dayofweek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

f = open(sys.argv[1])
f2 = open(sys.argv[2], "wt")
sen = []

for line in f:
    line = line.strip()
    uber = line.split(",")

    date = uber[1].split("/")
    day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
    sen.append("%s,%s %s,%s\n" % (uber[0],dayofweek[day],uber[2],uber[3]))

for s in sen:
   f2.write(s)
