import media #Imports the module "media" from the folder "Movies" to accsess the class "Movie"
import fresh_tomatoes #Imports the module "fresh_tomatoes" to create the movies webpage

#Instances of class "Movie"
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

rush_hour = media.Movie("Rush Hour", "An L.A and Shanghai cop team up to find the kidnapped daughter of a Chinese diplomat","https://medialifecrisis.com/files/images/articles/201702-Popgap/xRush-Hour-1998.jpg.pagespeed.ic.XAFW1DrQcT.jpg","https://www.youtube.com/watch?v=JMiFsFQcFLE")

bee_movie = media.Movie("Bee Movie", "A talking bee fights for rights in the human world","https://upload.wikimedia.org/wikipedia/en/6/62/Bee_movie_ver2.jpg","https://www.youtube.com/watch?v=VONRQMx78YI")

the_incredibles = media.Movie("The Incredibles", "A family of superheroes saves the planet from an imposter","http://vignette3.wikia.nocookie.net/pixar/images/4/44/Movie_poster_the_incredibles.jpg/revision/latest?cb=20100622151355","https://www.youtube.com/watch?v=eZbzbC9285I")

rouge_one = media.Movie("Rouge One: A Star Wars Story", "A group of unlikely heros bands together to steal plans to the Death Star from the Empire","http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg","https://www.youtube.com/watch?v=frdj1zb9sMY")

movies = [toy_story, avatar, rush_hour, bee_movie, the_incredibles, rouge_one] #Array containing all instances of class "Movie"
fresh_tomatoes.open_movies_page(movies) #Creates/opens movie trailers webpage using the array "movies" 
