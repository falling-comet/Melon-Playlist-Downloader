from pytube import YouTube
import glob
import os
from moviepy.editor import *
import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def youtube_to_mp3(link,path,filename):
    
    if not os.path.exists(os.path.join(path,'Temp (delete after downloading)')):
        os.mkdir(os.path.join(path,'Temp (delete after downloading)'))

    with HiddenPrints():


        if os.path.exists(os.path.join(path,'Temp (delete after downloading)',filename+'.mp4')):
            os.remove(os.path.join(path,'Temp (delete after downloading)',filename+'.mp4'))
        else:
            pass

        if os.path.exists(os.path.join(path,filename+'.mp3')):
            os.remove(os.path.join(path,filename+'.mp3'))
        else:
            pass

        yt = YouTube(link)

        yt.streams.filter().first().download(output_path=os.path.join(path,'Temp (delete after downloading)'),filename=filename)

        print('success')

        videoclip=VideoFileClip(os.path.join(path,'Temp (delete after downloading)',filename+'.mp4'))
        audioclip=videoclip.audio


        audioclip.write_audiofile(os.path.join(path,filename+'.mp3'))
        audioclip.close()

        videoclip.close()

        if os.path.exists(os.path.join(path,'Temp (delete after downloading)',filename+'.mp4')):
            os.remove(os.path.join(path,'Temp (delete after downloading)',filename+'.mp4'))
        else:
            pass
