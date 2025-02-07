import argparse
from media_processor.process import get_files_and_transcrible

parser = argparse.ArgumentParser()

parser.add_argument("directory_path", type=str, help="The path of directory you want to be processed")
parser.add_argument("--model", choices=["tiny", "base", "small","medium","large"], help="Whisper Model to be used for processing, by default: tiny",default="tiny")

if __name__ == "__main__":
    args = parser.parse_args()
    print(f"Your arguments are : directory_path={args.directory_path}  model={args.model}")
    get_files_and_transcrible(args.directory_path)