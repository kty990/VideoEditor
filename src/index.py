import sys
import os
import asyncio

# Get the parent directory of the current file
parent_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'

# Add the parent directory to the system path
sys.path.append(parent_dir)

from lib import display_test, project, preview
from lib import tempfile
from lib.event import Event

class Main:
    def __init__(self):
        self.NEW_PROJECT_OPENED = Event()
        self.proj = None
        self.app = display_test.Application()
        self.pWindow = preview.PreviewWindow(getattr(self.app,"pw_top",None))

        #TESTING PURPOSES:
        self.pWindow.canvas.configure(bg='orange')

        #Required code
        try:
            # asyncio.run(self.app.SetFrame(2, self.pWindow.canvas))
            self.app.SetFrame(2, self.pWindow.canvas)
            self.app.update()
            pass
        except Exception as e:
            print(f"Exception occured trying to set the preview frame into the window:\n{e}")
            quit()

        self.app.protocol("VM_DELETE_WINDOW",tempfile.mass_cleanup)
        self.NEW_PROJECT_OPENED.add_handler(tempfile.mass_cleanup)
        

    def file_open(self):
        filename = self.app.GetOpenFileName()
        if filename:
            if self.proj:
                self.proj.close()
            # try:
            self.proj = project.Project(filename)
            self.NEW_PROJECT_OPENED.fire(filename=filename)
            self.app.title(f"Video Editor | {filename}")
            # except Exception as e:
                # print(e)

main = Main()
display_test.open_file = main.file_open

main.file_open()
main.app.mainloop()