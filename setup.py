from setuptools import setup

setup(
    name="DeepVideoFER",
    version="0.1.0",
    description="A Library for Video Emotion Analysis. Facial Expression Recognition-Based Affective Computing for Emotion Detection in Videos using Deep Learning.",
    author="Francisco Reyne Pugh",
    author_email="freynep@udd.com",
    url="https://github.com/franciscoreyne/DeepVideoFER",
    packages=["DeepVideoFER"],
    install_requires=["deepface", "pandas", "matplotlib"],
)