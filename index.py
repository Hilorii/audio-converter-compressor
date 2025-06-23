# This script converts all audio files from the "z" folder to the "do" folder.
# You can customize the output format, bitrate, and sample rate as needed.
# It's useful for reducing the file size of audio files while maintaining acceptable quality.

import os
from pydub import AudioSegment

# Folder paths, you need to add them by yourself in the project.
source_folder = os.path.expanduser("./z")
output_folder = os.path.expanduser("./do")

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Convert all audio files
for filename in os.listdir(source_folder):
    if filename.endswith(('.mp3', '.wav', '.flac', '.ogg')):  # You can add more formats!
        audio_path = os.path.join(source_folder, filename)
        audio = AudioSegment.from_file(audio_path)

        # Convert to MP3 with 32 kbps bitrate and 32000 Hz sample rate
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")
        audio.set_frame_rate(32000).export(output_path, format="mp3", bitrate="32k")

print("Conversion completed!")
