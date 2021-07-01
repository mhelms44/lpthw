class Songs(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_a_song(self):
        for line in self.lyrics:
            print(line)

alphaand = Songs(["Reach into the nothingness",
                    "Consuming your sight"])
alphaand.sing_a_song()

mechanobiology = ["Contact, ended abruptly.","Signal lost, and without warning"]

mechanobiology_singer = Songs(mechanobiology)
mechanobiology_singer.sing_a_song()