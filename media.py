import webbrowser #Imports the module "webbrowser" from the python standard library

class Movie():
    """ This class provides a way to store movie related information"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): #Function which creates instance of class "Movie"
        #Instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self): #Function to show the trailer of an instance of class "Movie"
        webbrowser.open(self.trailer_youtube_url) #Opens a webpage of the trailer for the instance of class "Movie"
