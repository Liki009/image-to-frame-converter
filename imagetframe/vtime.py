from moviepy.editor import VideoFileClip
import time_conv

def get_video_duration_in_str(video_path):
    # create a VideoFileClip object
    try:
        video = VideoFileClip(video_path)

    # get the duration of the video in milliseconds
        duration_ms = int(video.duration * 1000)
        time_str= time_conv.convert_ms_to_hms(duration_ms)
        return time_str
    except Exception as e:
        time_str="00:00:00"
        return time_str
        
#mili=get_video_duration_in_str("test.mp4")
#print(mili)
