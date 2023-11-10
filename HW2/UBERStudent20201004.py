import sys
import calendar


dayofweek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

f = open(sys.argv[1])
f2 = open(sys.argv[2], "wt")
sen_dict = dict()

for line in f:
    line = line.strip()
    uber = line.split(",")

    date = uber[1].split("/")
    day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))

    sId = uber[0] + "," + dayofweek[day]
    if sId in sen_dict:
        val = sen_dict[sId].split(",")
        va11 = int(uber[2]) + int(val[0])
        val2 = int(uber[3]) + int(val[1])
    else:
        sen_dict[sId] =  uber[2] + "," + uber[3]


for s in sen_dict.keys():
    f2.write(s + " " + sen_dict[s] + "\n")

f.close()
f2.close()
