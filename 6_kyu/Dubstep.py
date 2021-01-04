def song_decoder(song):
    return ' '.join(l for l in song.split('WUB') if l)


print(song_decoder('AWUBWUBWUBBWUBWUBWUBC'))
