import random
import string

artists = 10
songs = 10
queueLength = 20
lastArtistsPlayed = [None, None]

## letter = artist
## number = song

playlist = [[string.ascii_letters[i] + str(x + 1) for x in range(songs)] for i in range(artists)]
print(playlist)

def isRepeatedArtist(genArtist):
    for i in lastArtistsPlayed:
        if genArtist == i:
            return True
        
def ChooseSong():
    _artist = random.randint(0, artists - 1)
    while isRepeatedArtist(_artist):
        _artist = random.randint(0, artists - 1)        
    lastArtistsPlayed.append(_artist)
    lastArtistsPlayed.pop(0)
    _song = random.randint(0, songs - 1)
    print(playlist[_artist][_song])

for i in range(queueLength):
    ChooseSong()

