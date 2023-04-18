import sys
import os
from PyQt5.QtWidgets import QApplication

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
        self.q_app = QApplication(sys.argv)
        self.app = display_test.Application(self.q_app)
        self.pWindow = preview.PreviewWindow(getattr(self.app,"pw_top",None))

        self.NEW_PROJECT_OPENED.add_handler(tempfile.mass_cleanup)

main = Main()
sys.exit(main.q_app.exec_())