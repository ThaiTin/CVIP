import os
import subprocess

ffmpeg_path = "C:/ffmpeg/ffmpeg.exe"
input_folder = "static/videos/org"
output_folder = "static/videos/org_safe"
new_fps = 10
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.mp4'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        print(f"Converting {filename}...")

        subprocess.run([
            ffmpeg_path,
            '-i', input_path,
            '-r', str(new_fps),
            '-vcodec', 'libx264',
            '-acodec', 'aac',
            '-movflags', '+faststart',
            output_path
        ])

print("✅ All videos converted.")
