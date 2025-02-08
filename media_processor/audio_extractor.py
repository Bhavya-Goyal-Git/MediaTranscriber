import shutil
import subprocess
import os
from .logger_config import logger

def extract_audio(video_path,audio_output_path):
    command = ["ffmpeg","-hide_banner","-loglevel", "error","-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_output_path]
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError as e:
        logger.exception(f"Error during audio extraction from file {video_path}: {e}")
    except FileNotFoundError:
        logger.exception(f"Trying to extract audio from {video_path} Error: ffmpeg not working!. Make sure it is installed and in the system PATH.")
    return False

def get_audio_name(video_path):
    filename, ext = os.path.splitext(os.path.basename(video_path))
    new_filename = "audio_" + filename + ".wav"
    new_path = os.path.join(os.path.dirname(video_path), new_filename)
    return new_path
    
def videos_to_audios(video_list):
    if not shutil.which("ffmpeg"):
        print("ffmpeg is not installed or not found in system PATH.")
        exit(1)
        
    audio_list = []
    
    for vid in video_list:
        aud = get_audio_name(vid)
        done = extract_audio(vid,aud)
        if(done):
            audio_list.append(aud)
    
    return audio_list