# Video Clipper

A simple command-line tool to create multiple clips from a video file using timestamps. Perfect for creating highlights or segments from long videos.

## Features

- Create multiple clips from a single video file
- Simple JSON configuration for clip timestamps
- Progress tracking for batch processing
- Preserves original video quality using stream copy
- Lightweight and easy to use

## Prerequisites

- Python 3.6+
- FFmpeg installed on your system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/erikthiart/VideoClipper.git
cd VideoClipper
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install tqdm ffmpeg-python
```

4. Install FFmpeg:
- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt-get install ffmpeg`
- Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html)

## Usage

1. Create a JSON file with your clip timestamps (e.g., `timestamps.json`):
```json
[
    {
        "start": "00:00:00",
        "end": "00:01:00"
    },
    {
        "start": "00:02:00",
        "end": "00:03:00"
    }
]
```

2. Run the script:
```bash
python video_clipper.py --input path/to/video.mp4 --timestamps timestamps.json --output-dir clips
```

### Arguments

- `--input`: Path to the input video file (required)
- `--timestamps`: Path to JSON file containing clip timestamps (required)
- `--output-dir`: Directory where clips will be saved (default: 'clips')

## Example

```bash
# Create clips directory
mkdir clips

# Run the script
python video_clipper.py --input my_video.mp4 --timestamps timestamps.json --output-dir clips
```

This will create numbered clips (clip_1.mp4, clip_2.mp4, etc.) in the specified output directory.

## Structure

```
video-clipper/
├── video_clipper.py    # Main script
├── timestamps.json     # Example timestamps file
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the unLicense - see the LICENSE file for details.

## Acknowledgments

- FFmpeg for video processing
- tqdm for progress bars
- ffmpeg-python for FFmpeg integration
