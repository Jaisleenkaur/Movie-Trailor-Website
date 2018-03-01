# Stores details of various movies
import media
import fresh_tomatoes
# Creating various insatnces of various movies
Dead_Pool = media.Movie("Dead Pool",
                        "Story on Marvel Comics.",
                        " deadpool.jpg",
                        "https://youtu.be/Xithigfg7dA")


Zoo_Topia = media.Movie("Zoo Topia",
                        "Story of city Zoo Topia",
                        "zootopia.jpg",
                        "https://youtu.be/yCOPJi0Urq4")


Three_idiots = media.Movie("Three idiots",
                           "Story of three college friends",
                           "3 idiots.jpg",
                           "https://www.youtube.com/watch?v=xvszmNXdM4w")


Harry_Potter = media.Movie(
                                "Harry Potter",
                                "Story of a boy",
                                "harry potter.jpg",
                                "https://youtu.be/VyHV0BRtdxo")

The_Croods = media.Movie(
    "The Croods",
    "American post-apocalyptic science fiction action adventurous film",
    "the croods.jpg",
    "https://youtu.be/4fVCKy69zUY")


# Creating an array called movies and store the Movie objects in that list.
movies = [
            Dead_Pool, Zoo_Topia, Three_idiots,
            Harry_Potter, The_Croods]

# using the python program fresh tomatoes for opening our website.
fresh_tomatoes.open_movies_page(movies)
