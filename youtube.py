import pafy
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import shutil


def emptyFolder():
    if os.path.isdir("videos"):
        shutil.rmtree("videos")
    os.mkdir("videos")


def downloadYoutube(url):
    video = pafy.new(url=url);
    video_d = video.getbest(preftype="mp4")

    video_d.download(filepath="videos/video."+video_d.extension)


def convertMp3():
    audio = VideoFileClip(os.path.join("videos", "video.mp4"))
    audio.audio.write_audiofile(os.path.join("videos", "song.mp3"))
    audio.close()
    return float(audio.duration)

def cutSong(duration):

    arrTimes = [[0,10],[duration/2 - 10, duration/2],[duration-15,duration-5]]
    for i,j in enumerate(arrTimes,start=1):
        ffmpeg_extract_subclip('videos/song.mp3', j[0], j[1], targetname=os.path.join("videos", f"cut{i}.mp3"))

def performanceY(url):
    emptyFolder()
    downloadYoutube(url)
    duration = convertMp3()
    cutSong(duration)
