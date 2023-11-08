f = open("movies_exp.txt")

genre_dict = dict()

for line in f:
    line = line.strip()
    movie = line.split("::")
    print(movie[2])

    genre = movie[2].split("|")
    for g in genre:
        g_id = g
        if g_id in genre_dict:
            genre_dict[g_id] += 1
        else:
            genre_dict[g_id] = 1

print(genre_dict)
