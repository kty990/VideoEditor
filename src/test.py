import cv2
import tkinter as tk
import os
import sys
from PIL import Image, ImageTk
from pydub import AudioSegment
from pydub.playback import play
import threading

# Get the parent directory of the current file
parent_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'

# Add the parent directory to the system path
sys.path.append(parent_dir)

from lib import tempfile

class App:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.temp_dir = tempfile.TemporaryDirectory()
        self.lock = threading.Lock()

        # Open video source
        self.vid = cv2.VideoCapture(video_source)

        # Open audio source
        self.audio = AudioSegment.from_file(video_source, format="mp4")

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.grid(row=0, column=0, padx=5, pady=5)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 50
        self.update()

        self.window.mainloop()

    def update(self):
        print("UPDATE")
        # Get a frame from the video source
        ret, frame = self.vid.read()
        with self.lock:
            #suffix="", delete=True, dir="./", subdir: str=None
            temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False, subdir=self.temp_dir.folder_name)
            if ret:
                # Convert the frame to PIL format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

            # Play the audio
            play(self.audio)

        # Remove the temporary file outside the lock to avoid blocking the audio playback thread
        os.unlink(temp_file.GetAbsDirectory())

        # Schedule the next update after the delay
        self.window.after(self.delay, self.update)

    def __del__(self):
        # Remove the temporary directory when the object is destroyed
        with self.lock:
            self.temp_dir.cleanup()


# Create a window and pass it to the Application object
s = App(tk.Tk(), "Tkinter and OpenCV", "./src/input.mp4")


"""

import cv2
import tkinter as tk
import os
import sys
from PIL import Image, ImageTk
from pydub import AudioSegment
from pydub.playback import play
import threading

# Get the parent directory of the current file
parent_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'

# Add the parent directory to the system path
sys.path.append(parent_dir)

from lib import tempfile
from lib import audio


a = audio.Audio()

class App:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.temp_dir = tempfile.TemporaryDirectory()
        self.lock = threading.Lock()

        # Open video source
        self.vid = cv2.VideoCapture(video_source)
        self.fps = self.vid.get(cv2.CAP_PROP_FPS)

        # Open audio source
        self.audio = AudioSegment.from_file(video_source, format="mp4")

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.grid(row=0, column=0, padx=5, pady=5)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 1 / self.fps

        temp_dir_2 = tempfile.TemporaryDirectory()
        temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False,
                                                    subdir=temp_dir_2.folder_name)
        # Start a new thread to play the audio
        t = threading.Thread(target=self.play_audio, args=(temp_file.name,))
        t.start()


        self.update()

        self.window.mainloop()

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()
        with self.lock:
            # suffix="", delete=True, dir="./", subdir: str=None
            # temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False, subdir=self.temp_dir.folder_name)
            if ret:
                # Convert the frame to PIL format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # # Start a new thread to play the audio
        # t = threading.Thread(target=self.play_audio, args=(temp_file.name,))
        # t.start()

        # Schedule the next update after the delay
        self.window.after(int(self.delay), self.update)

    def play_audio(self, temp_file_name):
        # Play the audio
        audio = AudioSegment.from_file(self.video_source, format="mp4")
        # audio = AudioSegment.from_wav(temp_file_name)
        audio.export(temp_file_name, format="wav")
        play(AudioSegment.from_wav(temp_file_name))

        # Remove the temporary file after the audio has finished playing
        os.unlink(temp_file_name)

    def __del__(self):
        # Remove the temporary directory when the object is destroyed
        with self.lock:
            self.temp_dir.cleanup()


# Create a window and pass it to the Application object

# window.protocol("VM_DELETE_WINDOW",tempfile.mass_cleanup)

# s = App(window, "Tkinter and OpenCV", "./src/input.mp4")

s = App(tk.Tk(), "Tkinter and OpenCV", "./src/input.mp4")


"""