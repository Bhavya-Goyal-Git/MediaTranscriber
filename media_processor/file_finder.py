import os
from .logger_config import logger
import magic

mime = magic.Magic(mime=True)

def is_audio_video(filepath):
    try:
        mime_type = mime.from_file(filepath)
    except OSError:
        return None
    return True if (mime_type.startswith("audio") or mime_type.startswith("video")) else False

def list_files(directory):
    
    if not os.path.isdir(directory):
        print(f"No such directory: {directory}")
        exit(1)

    file_list = []
    for root,_,files in os.walk(directory):
        for filee in files:
            file_path = os.path.join(root,filee)
            
            if not os.access(file_path, os.R_OK):
                logger.error(f"File: {file_path} couldn't be read!")
                continue
            
            is_media = is_audio_video(file_path)
            if is_media is None:
                logger.error(f"Permission errors in reading File: {file_path}")
            if is_media:
                file_list.append(file_path)
        
    return file_list