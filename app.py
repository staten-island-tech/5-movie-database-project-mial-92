import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for i in range(0, len(data)):
    print(data[i]["genres"])

search = input("What would you like to search for?")

