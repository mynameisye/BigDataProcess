import sys

f = open(sys.argv[1])

genre_dict = dict()

for line in f:
    line = line.strip()
    movie = line.split("::")

    genre = movie[2].split("|")
    for g in genre:
        g_id = g
        if g_id in genre_dict:
            genre_dict[g_id] += 1
        else:
            genre_dict[g_id] = 1

f = open(sys.argv[2], "wt")

for g, cnt in genre_dict.items():
    f.write("%s %d\n" % (g, cnt))

f.close()
