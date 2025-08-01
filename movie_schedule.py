current_movies = {'The Grinch': '11:00am',
                  'F1': '1:00pm',
                  'Superman': '4:00pm'}

print('We are showing the following movies:')
for key in current_movies:
    print(key)

movie = input('Which movie would you like the showtime for?\n')

if movie not in current_movies:
    print("Requested movie isn't playing")
else:
    print(movie, "is playing at", current_movies[movie])