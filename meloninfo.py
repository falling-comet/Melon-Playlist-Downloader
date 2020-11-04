import requests
from bs4 import BeautifulSoup

def get_key(url):
    k = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    key = k.url.split('plylstSeq=')[1]
    key = key.split('&ref')[0]
    return(key)

def get_song_list_playlist(key):
    result=[]

    url = 'https://www.melon.com/mymusic/playlist/mymusicplaylistview_listSong.htm?plylstSeq='+str(key)
    r = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(r.text,"html.parser")

    for item in soup.select("tr:has(#artistName)"):
        try:
            artist_name = item.select_one("#artistName > a[href*='goArtistDetail']")['title']
            song = item.select_one("a[href*='playSong']")['title']
            album = item.select_one("a[href*='javascript:melon.link.goAlbumDetail']")['title']
            artist_name = artist_name.split(" - ")[0]
            song = song.split(' 재생 - 새 창')[0]
            album = album.split(' - 페이지 이동')[0]

            result.append([song,artist_name,album])

        except TypeError:
            pass
    
    return result

def get_song_list_single(key):

    song_album_artist_list=[]

    url = 'https://www.melon.com/song/detail.htm?songId='+str(key)+'&ref=etc&snsGate=Y'
    r = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(r.text,"html.parser")

    song=soup.find_all("div", class_="song_name")
    song=song[0].text
    song=song.split()[1]

    artist_name=soup.find_all("a", class_="artist_name")
    artist_name=artist_name[0].text

    album=soup.find_all("div", class_="meta")
    album=album[0].text
    album=album.split('\n')[3]
    song_album_artist_list.append([song,artist_name,album])
    
    return song_album_artist_list

