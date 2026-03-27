
<p align="center">
  <img src="logo.png" width="1200"/>
</p>

<h1 align="center">DeepVideoFER</h1>

<p align="center">
  Video Emotion Analysis using Deep Learning
</p>

DeepVideoFER is a Python library for Video Emotion Analysis, specifically designed for Facial Expression Recognition (FER). It utilizes Deep Learning techniques to detect and analyze emotions in videos.



## Features

- Facial Expression Recognition (FER) in videos.
- Deep Learning-based emotion analysis.
- Easy integration into Python projects.
- Compatible with various video formats.

## Installation

You can install DeepVideoFER using pip:

```bash
pip install deepvideofer
```

## Usage

```python
import deepvideofer

# Load a video for emotion analysis
video_path = "path/to/your/video.mp4"
emotions = deepvideofer.analyze_emotions(video_path)

# Print the emotions detected in each frame
for frame_emotion in emotions:
    print(frame_emotion)

# Plot emotion trends over time
deepvideofer.plot_emotion_trends(emotions)
```

For more detailed usage instructions and examples, please refer to our [documentation](https://github.com/franciscoreyne/DeepVideoFER).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- DeepFace for providing the foundation for facial expression recognition.

## Contributing

We welcome contributions from the community. If you find issues or have suggestions for improvements, please open an issue or create a pull request.

## Contact

For questions or inquiries, please contact [Francisco Reyne](mailto:freynep@udd.cl).
