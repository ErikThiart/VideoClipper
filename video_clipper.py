import argparse
from pathlib import Path
from datetime import datetime
import subprocess
import json
from tqdm import tqdm

def timestamp_to_seconds(timestamp):
    """Convert timestamp (HH:MM:SS) to seconds."""
    time_obj = datetime.strptime(timestamp, '%H:%M:%S')
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def create_clip(input_file, start_time, end_time, output_file):
    """Create a clip from the video using ffmpeg."""
    try:
        # Calculate duration for progress bar
        duration = timestamp_to_seconds(end_time) - timestamp_to_seconds(start_time)
        
        # Set up ffmpeg command
        cmd = [
            'ffmpeg',
            '-i', str(input_file),
            '-ss', start_time,
            '-to', end_time,
            '-c', 'copy',
            str(output_file),
            '-y'
        ]
        
        print(f"Creating clip from {start_time} to {end_time}")
        process = subprocess.run(cmd, capture_output=True, text=True)
        
        if process.returncode == 0:
            print(f"Successfully created clip: {output_file}")
        else:
            print(f"Error creating clip: {process.stderr}")
            
    except subprocess.CalledProcessError as e:
        print(f"Error creating clip: {e}")

def main():
    parser = argparse.ArgumentParser(description='Create clips from a video file')
    parser.add_argument('--input', type=str, required=True, help='Path to input video file')
    parser.add_argument('--timestamps', type=str, required=True, help='JSON file containing clip timestamps')
    parser.add_argument('--output-dir', type=str, default='clips', help='Output directory for clips')
    
    args = parser.parse_args()
    
    # Set up paths
    video_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Check if video exists
    if not video_path.exists():
        print(f"Error: Video file not found at {video_path}")
        return
    
    # Load timestamps from JSON file
    try:
        with open(args.timestamps) as f:
            clips = json.load(f)
    except Exception as e:
        print(f"Error loading timestamps file: {e}")
        return
    
    print("Starting video processing...")
    
    # Process clips with progress bar
    for i, clip in enumerate(tqdm(clips, desc="Processing clips")):
        output_file = output_dir / f"clip_{i+1}.mp4"
        create_clip(video_path, clip['start'], clip['end'], output_file)

if __name__ == "__main__":
    main()
