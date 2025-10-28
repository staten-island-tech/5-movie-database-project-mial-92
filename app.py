import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

genre_list = ["Drama", 
              "Crime", 
              "War", 
              "Comedy", 
              "Fantasy", 
              "Independent", 
              "Noir", 
              "Thriller", 
              "Historical", 
              "Action", 
              "Romance", 
              "Western", 
              "Mystery", 
              "Musical", 
              "Science Fiction", 
              "Disaster", 
              "Political", 
              "Family", 
              "Adventure", 
              "Biography", 
              "Suspense", 
              "Animated"]
print(genre_list)
answer = input("What genre are you looking for?")
for i in range(0, len(data)):
    if answer in data[i]["genres"]:
        print(data[i]["title"])
