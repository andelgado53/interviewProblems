movies = [60, 60, 120, 130, 70, 70]
flight_lengt = 120

def inflight_movies_n_square(flight_lengt, movie_lengths):
    lengths = {}

    for movie in movie_lengths:
        lengths[movie] = lengths.get(movie, 0) + 1
    print(lengths)
    for first_movie in movie_lengths:
        if first_movie >= flight_lengt:
            continue
        else:
            key_to_find = flight_lengt - first_movie
            second_movie = lengths.get(key_to_find, 0)
            if (first_movie == key_to_find and second_movie > 1) or (first_movie != key_to_find and second_movie > 0):
                return True
    return False

print(inflight_movies_n_square(flight_lengt, movies))
