def is_good_score(name):
    for film in movies:
        if film["name"] == name:
            if film["imdb"] >= 5.5:
                return True
            else:
                return False

    #print(movies[1]["name"])


def list_of_movies(score):
    my_list = []
    for film in movies:
        if film["imdb"] >= score:
            my_list.append(film)
    return my_list


def category_list(category):
    my_list = []
    for film in movies:
        if film["category"] == category:
            my_list.append(film)
    return my_list


def average_in_list(my_list):
    imdb = 0
    for film in my_list:
        imdb += film["imdb"]
    imbd = round(imdb/len(my_list), 2)
    return imbd


def average_in_category(category):
    imdb = 0
    count = 0
    for film in movies:
        if film["category"] == category:
            imdb += film["imdb"]
            count += 1
    imdb = round(imdb/count, 2)
    return imdb



movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

name = input("Enter: ")
print(average_in_category(name))
