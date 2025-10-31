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
for i in range(0, len(data)):
    print(data[i]["title"])
    print(f"These are the genres: {genre_list}")
    genre = input("What genre are you looking for? ")
    year = input("What year, 1961 - 2023 ")
    if genre in data[i]["genres"] and year in str(data[i]["year"]):
        print(data[i]["title"])




