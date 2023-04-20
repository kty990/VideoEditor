from PyQt5.QtWidgets import QSplitter, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor

# from lib import splinter
# from lib.splinter import SplinterFunction

class Time:
    def __init__(self, seconds: int = None, minutes: int = None, hours: int = None):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

class VideoNode:
    def __init__(self, frame=None, next=None, prev=None):
        self.frame = frame
        self.next = next
        self.prev = prev
        self.start_time = Time(0,0,0)
        self.duration = Time(0,0,0)

class VideoTrack(QWidget):
    def __init__(self, parent=None, track_number: int = 1):
        super().__init__(parent)

        self.r_frame = VideoNode() #Root frame
        self.track_number = track_number

    def next_frame(self):
        return self.r_frame.next

    def prev_frame(self):
        return self.r_frame.prev
    
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QPen(QColor(255, 0, 0), 5))
        qp.drawEllipse(50, 50, 300, 200)
        qp.end()
    
    """
    Insert clip based on starting position
    - Moves other clips to make room for said clip
    - Handles frame setting (audio and video)
    """
    def insert(self, start: Time = None, frame=None):
        # Create a new node with the given frame and audio
        new_node = VideoNode(frame=frame)
        
        # If the root node is empty, set it to the new node
        if not self.r_frame.frame:
            self.r_frame = new_node
            return
        
        # Traverse the linked list to find the node after which to insert the new node
        current_node = self.r_frame
        while current_node.next and current_node.next.frame and current_node.next.frame.start_time < start: ############################################################### frame.start_time
            current_node = current_node.next
        
        # Insert the new node after the current node
        new_node.prev = current_node
        new_node.next = current_node.next
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node
        
        # Update the start times of the subsequent nodes
        while current_node.next:
            current_node = current_node.next
            current_node.frame.start_time += new_node.frame.duration ############################################################ frame.duration (could be a still image that plays for an extended period of time, adding more sound data to a singular node)
        
        # Update the start time of the new node
        new_node.frame.start_time = start

    """
    Remove video content from start time to end time and return the removed frames
    """
    def cut(self, start: Time = None, end: Time = None):
        # Traverse the linked list to find the first node to remove
        current_node = self.r_frame
        while current_node and current_node.frame and current_node.frame.start_time < start:
            current_node = current_node.next
        
        # Remove nodes between start and end times and store them in a list
        removed_frames = []
        while current_node and current_node.frame and current_node.frame.start_time < end:
            removed_frames.append(current_node.frame)
            next_node = current_node.next
            if current_node.prev:
                current_node.prev.next = next_node
            else:
                self.r_frame = next_node
            if next_node:
                next_node.prev = current_node.prev
            current_node = next_node
        
        return removed_frames

"""
A video excerpt contains all tracks between given intervals of time
"""
class VideoExerpt:
    def __init__(self, filetype: str = None, tracks: list[VideoTrack] = None):
        self.filetype = filetype
        self.tracks = tracks
        self.tracks = sorted(self.tracks, key=lambda x: x.track_number)
        self.splintered_render = None

        # self.splinter_function = splinter.splinter_functions[filetype]
        # assert isinstance(self.splinter_function, SplinterFunction), "self.splinter_function is not an instance of SplinterFunction"

        pass

    def run(self):
        self.splinter_function.run(self.tracks)

    def save_splintered_render(self):
        # assert(isinstance(self.splintered_render, splinter.SplinteredRender), f"Expected type 'splinter.SplinteredRender', got {type(self.splintered_render)}")
        pass

    def add_subtitles(self):
        pass