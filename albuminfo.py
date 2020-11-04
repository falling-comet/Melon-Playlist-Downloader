import requests

def song_syntax_fixer(song):
    song=song.replace("'",'')
    song=song.replace(".",'')
    song=song.replace("<",'')
    song=song.replace(">",'')
    song=song.replace(":",'')
    song=song.replace('"','')
    song=song.replace("/",'')
    song=song.replace("|",'')
    song=song.replace("?",'')
    song=song.replace("*",'')
    return song


def get_album_art_high(song,artist_name,album):
    API_KEY = 'b73672ba11b09300fdf7bcd2a2db1863'
    
    song=song.split('(')[0]
    artist_name=artist_name.split('(')[0]

    headers = {
    'user-agent': 'Mozilla/5.0'
    }

    payload = {
    'api_key': API_KEY,
    'method': 'album.getinfo',
    'artist': artist_name,
    'album': album,
    'autocorrect':'1',
    'format': 'json'
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)

    try:
        return r.json()['album']['image'][3]['#text']
    except KeyError:
        return ''


def get_album_art_low(song,artist_name,album):
    API_KEY = 'b73672ba11b09300fdf7bcd2a2db1863'

    song=song.split('(')[0]
    artist_name=artist_name.split('(')[0]

    headers = {
    'user-agent': 'Mozilla/5.0'
    }

    payload = {
    'api_key': API_KEY,
    'method': 'album.search',
    'limit': '1',
    'album': album,
    'format': 'json'
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    
    try:
        return r.json()['results']['albummatches']['album'][0]['image'][3]['#text']
    except KeyError:
        return ''

def get_music_inf(song,artist_name,album):
    API_KEY = 'b73672ba11b09300fdf7bcd2a2db1863'
    
    song=song.split('(')[0]
    artist_name=artist_name.split('(')[0]

    headers = {
    'user-agent': 'Mozilla/5.0'
    }

    payload = {
    'api_key': API_KEY,
    'method': 'track.getinfo',
    'autocorrect':'1',
    'track' : song,
    'artist': artist_name,
    'format': 'json'
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)

    try:
        return r.json()['track']['album']['image'][3]['#text']
    except KeyError:
        return ''