from lib.playback import Time
from lib.playback import VideoTrack
from datetime import datetime

import cv2
import numpy as np


class SplinteredRender:
    def __init__(self, start: Time = Time(0,0,0), fps: int = 60, width: int = 1920, height: int = 1080):
        self.data = None
        self.start_time = start
        self.fps = fps
        self.width = width
        self.height = height

class SplinterFunction:
    def __init__(self, tracks: list[VideoTrack] = []):
        self.tracks = tracks
        self.filename = str(datetime.now().isoformat())
        self.video_writer = cv2.VideoWriter(self.filename, cv2.VideoWriter_fourcc(*'mp4v'), self.fps, (self.width, self.height))
        self.render = SplinteredRender()

    def run(self):
        #Combine all tracks into 1 clip
        pass

class MP4(SplinterFunction):
    def __init__(self, tracks: list[VideoTrack] = []):
        super().__init__(tracks)

    def run(self):
        #Combine all tracks into 1 clip
        pass


splinter_functions = {
    "mp4" : MP4
}