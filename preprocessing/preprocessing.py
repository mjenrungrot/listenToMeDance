import pytube
import uuid
import pandas as pd
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

def downloadSongs(csv_path, fps=30, audio_fs=44100):
  df = pd.read_csv(csv_path)

  for idx, song in df.iterrows():  
    song_identifier = str(uuid.uuid4())
    # Download song
    yt = pytube.YouTube(song['youtube_url']).streams.filter(file_extension='mp4').first().download(filename='tmp')
    print("Download {:} successfully".format(song['youtube_url']))

    # Trim video
    (start_second, end_second) = (song['start_second'], song['end_second'])

    # Preprocess fps + bitrate
    clip = VideoFileClip('tmp.mp4').subclip(start_second, end_second)
    clip.write_videofile(song_identifier + '.mp4', fps=fps)
    ffmpeg_extract_audio(song_identifier + '.mp4', 
                         song_identifier + '.mp3',
                         bitrate=128e3,
                         fps=audio_fs)
    print("Finished preprocessing {:} [{:} - {:}]".format(song_identifier, song['song_name'], song['artist']))

if __name__ == '__main__':
  downloadSongs('mini_dataset.csv')
