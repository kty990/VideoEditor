PROJECT_FILETYPE = ".vproj"

class Project:
    def __init__(self, project_name: str = None):
        if project_name == "":
            raise Exception("Can't open 'None' project.")
        self.name = project_name
        self.tracks = [] #Type = playback.VideoTrack
        self.splintered_renders = [] #Type = splinter.SplinterFunction


    def __repr__(self):
        return f"<< Project >>\nName: {self.name}"

    """
    Reads a project
    """
    def read(self):
        pass

    """
    auto-save a project
    """
    def auto_save(self):
        pass

    """
    Closes a project
    """
    def close(self, save):
        if save:
            #Save before closing
            pass