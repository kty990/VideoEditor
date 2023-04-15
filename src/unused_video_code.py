import cv2
from pydub import AudioSegment
from pydub.playback import play
from lib import playback, display, project

if __name__ == "__main__":
    """EVERYTHING AFTER THIS POINT WILL BE USED EVENTUALLY"""
    # Create a VideoCapture object to read the video file
    cap = cv2.VideoCapture('video_file.mp4')

    # Read the audio file using PyDub
    audio = AudioSegment.from_file('audio_file.mp3', format='mp3')

    # Create a window to display the video
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)

    # Loop through the frames of the video
    while True:
        # Check if the frame was successfully read
        if not ret:
            break
        
        # Display the current frame in the window
        cv2.imshow('video', frame)
        
        # Play the audio corresponding to the current frame
        t1 = cap.get(cv2.CAP_PROP_POS_MSEC) # current frame time in milliseconds
        t2 = t1 + 33.33 # duration of a frame in milliseconds
        play(audio[t1:t2])
        
        # Wait for a key press and check if the user wants to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Read the next frame of the video
        ret, frame = cap.read()

    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()













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
