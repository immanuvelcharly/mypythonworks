movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}

]

lst=[1,20,3,30]
max(lst)

movie_name=[ m.get("name") for m in movies]

# genre_movies=[m.get("name")for m in movies if "mystery" in m.get("generes")]

top_rated_movies=max(movies,key=lambda m:m.get("rating"))

year_filter=[m.get("name")for m in movies if m.get("year")==2023]

print(movie_name)

movie_sorted=sorted(movies,reverse=True,key=lambda m:m.get("rating"))
print(movie_sorted)

malayalam_movienames=[m.get("name")for m in movies if m.get("language")=="malayalam"]
print(malayalam_movienames)
