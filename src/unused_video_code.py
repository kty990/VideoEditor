import cv2
from pydub import AudioSegment
from pydub.playback import play
from lib import playback, display, project

if __name__ == "__main__":
    exit(-1)
    """EVERYTHING AFTER THIS POINT WILL BE USED EVENTUALLY"""
    
    """USED TO STORE FRAMES AS 2D arrays (BGR not RGB)"""
    import cv2

    # Open the video file
    cap = cv2.VideoCapture('path/to/video/file.mp4')

    # Read the first frame
    ret, frame = cap.read()

    # Loop through the video frames
    while ret:
        # Store the BGR frame as a 3D array
        # (assuming the video has a resolution of 640x480)
        frame_array = frame.reshape(480, 640, 3)

        # Do something with the frame array (e.g. save it to a file)

        # Read the next frame
        ret, frame = cap.read()

    # Release the video capture object
    cap.release()













    """USED TO STACK MULTIPLE VIDEOS"""
    from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip

    # Load the videos
    video1 = VideoFileClip("video1.mp4")
    video2 = VideoFileClip("video2.mp4")

    # Create a CompositeVideoClip object with the two videos stacked on top of each other
    composite_clip = CompositeVideoClip([video1, video2.set_position((0, video1.h))])

    # Set the duration of the composite clip to the longer of the two input clips
    duration = max(video1.duration, video2.duration)
    composite_clip = composite_clip.set_duration(duration)

    # Write the composite clip to a new video file
    composite_clip.write_videofile("stacked_video.mp4")

    """ USED TO SAVE A TRACK TO A FILE """
    from moviepy.editor import VideoClip

    # Define a function to generate frames from a VideoTrack object
    def make_frame(t):
        # Set the current frame to the frame at time t in the VideoTrack
        current_frame = video_track.get_frame_at_time(t)

        # Return the image data as a NumPy array
        return current_frame.to_ndarray()

    # Create a VideoClip object using the make_frame function and the duration of the VideoTrack
    video_clip = VideoClip(make_frame, duration=video_track.duration)

    # Write the VideoClip to an MP4 file
    video_clip.write_videofile("output.mp4")
