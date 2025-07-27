import cv2
import os
import math

# --- Settings ---
input_folder = 'static/videos/org'        # Input folder
output_folder = 'static/videos/org_10'    # Output folder
new_fps = 10                               # Desired FPS

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all MP4 files
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.mp4'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        print(f"Processing: {filename}")

        cap = cv2.VideoCapture(input_path)
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        skip_interval = int(original_fps / new_fps)
        if skip_interval < 1:
            skip_interval = 1  # Avoid division by zero or too many frames

        # Output writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' or 'XVID'
        out = cv2.VideoWriter(output_path, fourcc, new_fps, (width, height))

        frame_index = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if frame_index % skip_interval == 0:
                out.write(frame)

            frame_index += 1

        cap.release()
        out.release()

print("✅ All videos converted to", new_fps, "FPS while preserving duration.")
