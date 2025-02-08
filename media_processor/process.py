from .file_finder import list_files
from .audio_extractor import videos_to_audios

def get_files_and_transcrible(directory_name):
    #getting audios and videos in the directory
    audio_files,video_files = list_files(directory_name)
    
    #convert videos to audios for transcription
    audio_files.extend(videos_to_audios(video_files))
    
    #transcribing and saving using whisper
    
    
    print(f"audio : {audio_files} \nvideo : {video_files}")