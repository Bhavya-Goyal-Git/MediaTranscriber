import whisper
import torch
import os
import json
from .logger_config import logger

def load_model(model_name):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading model: {model_name}")
    model = whisper.load_model(model_name).to(device)
    return model

def get_text_name(audio_path):
    filename, ext = os.path.splitext(os.path.basename(audio_path))
    new_filename = "transcribed_" + filename + ".json"
    new_path = os.path.join(os.path.dirname(audio_path), new_filename)
    return new_path

def transcribe_audios(audio_list,model_name):
    model = load_model(model_name)
    
    for audio in audio_list:
        try:
            print(f"Transcribing : {audio}")
            result = model.transcribe(audio)
        except:
            logger.exception(f"Could not transcribe : {audio}")
            continue
        
        filtered_result = {
            "text": result["text"],
            "language": result["language"],
            "segments": [
                {"start": seg["start"], "end": seg["end"], "text": seg["text"]}
                for seg in result["segments"]
            ]
        }
        
        output_name = get_text_name(audio)
        try:
            with open(output_name, "w", encoding="utf-8") as f:
                json.dump(filtered_result, f, ensure_ascii=False, indent=4)
            print(f"Transcription for : {audio} completed.")
        except:
            logger.exception(f"Could not save transcription result for : {audio}")