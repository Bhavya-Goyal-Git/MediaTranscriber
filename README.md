# Media Transcriber

## Instructions
This project provides a transcription pipeline using OpenAI's Whisper model. It takes in name of directory as input and transcribes all audio/video files in the directory or any of its subdirectories.

## Setup Instructions

### 1. Install FFmpeg
FFmpeg is required for audio processing.
- On Ubuntu: `sudo apt install ffmpeg`
- On Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add it to your system PATH.

### 2. Install CUDA Driver (if you have a GPU)
Ensure you have the correct CUDA driver installed for your GPU. Refer to the [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) for installation instructions.

### 3. Create and Activate a Python Virtual Environment
Run the following commands:

```sh
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux:
source venv/bin/activate
```

### 4. Install Whisper
Run:
```sh
pip install openai-whisper
```

### 5. Install `python-magic`
- **Windows:**
  ```sh
  pip install python-magic-bin
  ```
- **Linux:**
  ```sh
  pip install python-magic
  sudo apt install libmagic1
  ```

### 6. Install PyTorch (Based on Your CUDA Version)
Visit the [PyTorch Installation Guide](https://pytorch.org/get-started/locally/) and follow the instructions based on your CUDA version. Typically, you can install PyTorch using:

```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cuXX
```
Replace `cuXX` with your CUDA version (e.g., `cu118` for CUDA 11.8).

If using CPU only, install PyTorch with:
```sh
pip install torch torchvision torchaudio
```

---
You are now ready to use the project!

## Running the project

```sh
python run.py <directory_name> --model <model_name>

#You can omit model name, by default it uses 'tiny'
python run.py <directory_name>
```