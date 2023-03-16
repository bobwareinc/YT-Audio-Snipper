from pytube import YouTube
import os

def download_audio(video_url: str, start_time: str, end_time: str):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    filename = f'{yt.title}.mp4'
    stream.download(filename=filename)
    
    new_filename = filename.rsplit('.', 1)[0] + '.wav'
    
    start_time_seconds = sum(int(x) * 60 ** i for i,x in enumerate(reversed(start_time.split(':'))))
    end_time_seconds = sum(int(x) * 60 ** i for i,x in enumerate(reversed(end_time.split(':'))))
    
    os.system(f'ffmpeg -y -i "{filename}" -ss {start_time_seconds} -to {end_time_seconds} "{new_filename}"')
    os.remove(filename)

# Example usage:
download_audio('ENTER_THE_YOUTUBE_URL_HERE', 'START_TIME', 'END_TIME')