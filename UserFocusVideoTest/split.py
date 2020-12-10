""" Helper File to Split Videos """

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

source_video = "samplevid.mp4"
split_times = ['0-60', '60-80', '100-120']

def video_splitter(source_video, split_times):
    split_times = [x.strip() for x in split_times] 
    for time in split_times:
        starttime = int(time.split("-")[0])
        endtime = int(time.split("-")[1])
        ffmpeg_extract_subclip(source_video, starttime, endtime, targetname=str(split_times.index(time)+1)+".mp4")


video_splitter(source_video, split_times)