PROJECT_FILETYPE = ".vproj"
from lib.event import Event
from lib import playback

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon

def ProjectError(error: str = "An error has occured!"):
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Critical)
    error_box.setWindowIcon(QIcon('./res/icon.ico'))
    error_box.setWindowTitle("Error")
    error_box.setText(error)
    error_box.setStandardButtons(QMessageBox.Ok)
    error_box.exec_()

    
class Project:
    def __init__(self, project_name: str = None):
        if project_name == "":
            raise Exception("Can't open 'None' project.")
        self.name = project_name
        self.tracks = [] #Type = playback.VideoTrack
        self.splintered_renders = [] #Type = splinter.SplinterFunction
        self.ON_PROJ_CLOSE = Event()


    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"<< Project >>\nName: {self.name}"

    """
    Reads a project
    """
    def open(self):
        if self.name.endswith(PROJECT_FILETYPE):
            pass
        else:
            ProjectError(f"Attempt to open a non {PROJECT_FILETYPE} file")
            self.close()

    """
    auto-save a project
    """
    def auto_save(self):
        pass

    """
    Closes a project
    """
    def delete_track(self, track):
        pass

    def close(self):
        # To be used when files are used
        self.ON_PROJ_CLOSE.fire()
        pass