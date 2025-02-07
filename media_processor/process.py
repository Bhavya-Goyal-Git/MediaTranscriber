from .file_finder import list_files

def get_files_and_transcrible(directory_name):
    #getting audios and videos in the directory
    media_files = list_files(directory_name)
    
    #transcribing and saving using whisper
    
    
    print(media_files)