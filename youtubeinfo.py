from youtubesearchpython import SearchVideos
import json

def search_youtube(song):
    search = SearchVideos(song, offset = 1, mode = "json", max_results = 1)
    result=json.loads(search.result())
    return(result["search_result"][0]["link"])
