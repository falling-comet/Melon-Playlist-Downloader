from moviepy.editor import *

mp4_file = r'E:\VID_20180308_141907.mp4'
mp3_file = r'E:\VID_20180308_141907.mp3'

videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)

audioclip.close()
videoclip.close()