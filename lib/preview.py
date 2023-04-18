import cv2
import os
from PIL import Image, ImageQt

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from pydub import AudioSegment
from pydub.playback import play
import threading
from lib import tempfile

class PreviewWindow:
    def __init__(self, video_source: str = None):
        # Create the main application window
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.window.resize(800, 600)
        self.window.setWindowTitle("Preview Window")

        # Create a widget to contain the video canvas
        self.central_widget = QtWidgets.QWidget()
        self.window.setCentralWidget(self.central_widget)

        # Create a canvas that can fit the above video source size
        self.canvas = QtWidgets.QLabel(self.central_widget)
        self.canvas.resize(800, 600)

        self.video_source = video_source
        self.current_playback = None
    
    def __del__(self):
        # Remove the temporary directory when the object is destroyed
        if not hasattr(self, 'lock'):
            return
        with self.lock:
            self.temp_dir.cleanup()

    def start(self):
        self.temp_dir = tempfile.TemporaryDirectory(dir='./')
        self.lock = threading.Lock()

        # Open video source
        self.vid = cv2.VideoCapture(self.video_source)
        self.fps = self.vid.get(cv2.CAP_PROP_FPS)

        # Open audio source
        self.audio = AudioSegment.from_file(self.video_source, format="mp4")
        
        def foo():
            temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False, dir='./', subdir=self.temp_dir.folder_name)
            # Start a new thread to play the audio
            t = threading.Thread(target=self.play_audio, args=(temp_file.name,))
            t.start()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = int(round((1 / self.fps)*1000))
        print(f"DELAY: {self.delay}")
        self.update()

        foo()
        self.window.after(2*1000, self.update)
        self.window.show()
        self.app.exec_()

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()
        with self.lock:
            if ret:
                # Convert the frame to QImage format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                qimage = ImageQt.ImageQt(Image.fromarray(frame))
                pixmap = QtGui.QPixmap.fromImage(qimage)
                self.canvas.setPixmap(pixmap)

        # Schedule the next update after the delay
        self.window.after(self.delay, self.update)

    """
    EVERYTHING BELOW THIS POINT HAS TO CHANGE ONCE THE NODES ARE BEING USED
    - audio.py will be used to break the audio into 1 second chunks
    - based on the fps of the track, n number of frames will be chunked together in a "NodeChunk" object
        - Have to create NodeChunk class
    """

    def play_audio(self, temp_file_name, volume: float = 1.0):
        # Play the audio
        audio = AudioSegment.from_file(self.video_source, format="mp4")
        audio.export(temp_file_name, format="wav")
        self.current_playback = play(AudioSegment.from_wav(temp_file_name))
        self.current_playback.set_volume(volume)

        # Remove the temporary file after the audio has finished playing
        os.unlink(temp_file_name)

    def set_volume(self, volume: float = 1.0):
        self.media_player.setVolume(int(volume * 100))
        
    def pause_audio(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        
    def stop_audio(self):
        self.media_player.stop()
        
    def mediaStateChanged(self, state):
        # Handle the media player state change
        if state == QMediaPlayer.StoppedState:
            self.media_player.setPosition(0)
        elif state == QMediaPlayer.PausedState:
            self.timer.stop()
        elif state == QMediaPlayer.PlayingState:
            self.timer.start(self.delay)