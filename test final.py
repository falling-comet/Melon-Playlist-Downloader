from albuminfo import *
from meloninfo import *
from youtubeinfo import *
from downloader import *
import eyed3
import os
import multiprocessing

global output_path

output_path = r"C:\Users\andyy\OneDrive\바탕 화면\python\melontoyoutube\test"

melon_url="http://kko.to/lVk4vD3Do"


def dowload(item):

    song , artist_name , album = item

    song = song_syntax_fixer(song)

    youtube_result = search_youtube(item[0]+' '+item[1])

    youtube_to_mp3(youtube_result,output_path,song)

    song_file = eyed3.load(os.path.join(output_path,song+".mp3"))

    song_file.tag.artist = artist_name
    
    song_file.tag.album = album

    art=get_music_inf(song,artist_name,album)

    if art=='':
        art=get_album_art_high(song,artist_name,album)

    if art=='':
        art=get_album_art_low(song,artist_name,album)
    
    if art=='':
        print('****************************No artwork availiable****************************')
    
    print(art)

    try:
        response = requests.get(art)
        imagedata = response.content
        song_file.tag.images.set(3,imagedata,"image/png",u"None")
        song_file.tag.save()

    except requests.exceptions.MissingSchema:
        print('fuck')


    
    song_file.tag.save()

    print('done')

key = get_key(melon_url)

print(key)

songlist = get_song_list_playlist(key)

print(songlist)

from multiprocessing import Pool


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(dowload,songlist))