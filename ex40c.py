# Creates a class named Song
class Song(object):
    # Instantiate or create an object from the class; creating multiple individual modules
    # self refers to empty object python creates and you can assign variables to it
    # Here we have self and lyrics and assign self.lyrics to lyrics.
    def __init__(self, lyrics):
        self.lyrics = lyrics
    # Function that has self (which we set to lyrics) passed to it
    # The function has a for loop that reads the lines assigned to self.lyrics and
    # for each line prints to stdout. 
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Creates a variable called happy_bday with a list of strings assigned to it, and then sees we are calling
# a class we defined called Song and are passing the list of strings to the variable called lyrics which
# will then assign to self.lyrics.  
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued,"
                    "So I'll stop right there"])
# Since classes give us a blueprint for creating many individual copies of an object, we can perform the same
# process on a different variable without interfering with the previous object. 
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
# Calls the sing_me_a_song function from the Song class using the previously defined lyrics for each object.
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()