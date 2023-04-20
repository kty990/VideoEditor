import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt


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
        self.NEW_PROJECT_CREATED = Event()
        self.proj = None
        self.q_app = QApplication(sys.argv)
        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor(50,255,145))
        self.q_app.setPalette(palette)
        self.q_app.setStyleSheet("""
            QDockWidget {
                background-color: #7d7d7d;
                padding: 0;
                margin: 0;
                color: white;
                font-size: 18px;
                padding: 0;
                margin: 0;
            }

            #top_widget {
                background-color: #999999;
                border-radius: 15px;

                border-color: #000000;
                border-style: inset;
                border-width: 1px;
            }

            QHBoxLayout {
                border-color: #ffffff;
                border-style: inset;
                border-width: 100px;
            }

            QMainWindow {
                padding: 0;
                margin: 0;
            }

            QSplitter {
                background-color: #c8c8c8;
                color: black;
                border-color: black;
                border-style: inset;
                border-width: 1px;
                border-radius: 25px;
                font-size: 18px;
            }
        """)
        self.app = display_test.Application(self.q_app, self)
        self.pWindow = preview.PreviewWindow(self.app.top)
        self.pWindow.canvas.setObjectName("top_widget")
        self.app.qTopLayout.insertWidget(1,self.pWindow.canvas)
        self.app.qTopLayout.setStretchFactor(self.pWindow.canvas, 1)

        def cleanup(p):
            tempfile.mass_cleanup()

        self.NEW_PROJECT_OPENED.add_handler(cleanup)

        def debug(p):
            print(f"self.NEW_PROJECT_OPENED fired!\n\tp: {p}")

        def mod_proj(filename):
            if self.proj:
                self.proj.close()
            self.proj = project.Project(filename)
            print(self.proj)
        
        self.NEW_PROJECT_OPENED.add_handler(debug)
        self.NEW_PROJECT_OPENED.add_handler(mod_proj)

main = Main()
sys.exit(main.q_app.exec_())