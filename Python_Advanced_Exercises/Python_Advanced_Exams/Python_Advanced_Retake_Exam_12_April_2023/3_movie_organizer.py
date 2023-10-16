def movie_organizer(*movies):
    movies_collection = {}
    for movie_name, genre in movies:
        if genre not in movies_collection.keys():
            movies_collection[genre] = []
        movies_collection[genre].append(movie_name)

    sorted_collection = sorted(movies_collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    for genre_, movies_ in sorted_collection:
        result += f'{genre_} - {len(movies_)}\n'
        for movie in sorted(movies_):
            result += f'* {movie}\n'

    return result


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print()

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print()

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
