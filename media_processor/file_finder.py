import os
from .logger_config import logger
import magic

mime = magic.Magic(mime=True)

def is_audio_video(filepath):
    try:
        mime_type = mime.from_file(filepath)
    except OSError:
        return None
    if mime_type.startswith("audio"):
        return True,"audio"
    elif mime_type.startswith("video"):
        return True,"video"
    return False,None

def list_files(directory):
    
    if not os.path.isdir(directory):
        print(f"No such directory: {directory}")
        exit(1)

    audio_list,video_list = [],[]
    for root,_,files in os.walk(directory):
        for filee in files:
            file_path = os.path.join(root,filee)
            
            if not os.access(file_path, os.R_OK):
                logger.error(f"File: {file_path} couldn't be read!")
                continue
            
            is_media = is_audio_video(file_path)
            if is_media is None:
                logger.error(f"Permission errors in reading File: {file_path}")
            elif is_media[0]:
                if is_media[1]=="audio":
                    audio_list.append(file_path)
                else:
                    video_list.append(file_path)
        
    return audio_list,video_list