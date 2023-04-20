import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QDockWidget, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QSplitter
from PyQt5.QtCore import Qt

# Get the parent directory of the current file
parent_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'

# Add the parent directory to the system path
sys.path.append(parent_dir)

from lib import project
from lib import playback

FILE_TYPES = [
    ("Project", f"*{project.PROJECT_FILETYPE}"),
    ("All Files", f"*")
]

class Application(QMainWindow):

    def __init__(self, app, index_main):
        super().__init__()

        self.app = app
        self.index_main = index_main

        self.initUI()

    def initUI(self):

        # Create a menu bar and add a "Open" action to it
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        qTopLayout = QHBoxLayout()

        previewWindow_contents = QTextEdit()
        previewWindow_layout = QVBoxLayout()
        previewWindow_layout.addWidget(previewWindow_contents)
        previewWindow_widget = QWidget()
        previewWindow_widget.setLayout(previewWindow_layout)

        self.attributesWindow_contents = QTextEdit()
        attributesWindow_layout = QVBoxLayout()
        attributesWindow_layout.addWidget(self.attributesWindow_contents)
        attributesWindow_widget = QWidget()
        attributesWindow_widget.setLayout(attributesWindow_layout)

        settingsWindow_contents = QTextEdit()
        settingsWindow_layout = QVBoxLayout()
        settingsWindow_layout.addWidget(settingsWindow_contents)
        settingsWindow_widget = QWidget()
        settingsWindow_widget.setLayout(settingsWindow_layout)

        # Create another QDockWidget with a QVBoxLayout
        dock2 = QDockWidget("Tracks", self)
        dock2.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        dock2_contents = QSplitter(Qt.Vertical)
        dock2_contents.setStyleSheet("""
            QSplitter::handle:horizontal {
                background-color: #ccffff;
            }
            QSplitter::handle:vertical {
                background-color: black;
            }
        """)

        for xc in range(3):
            v = playback.VideoTrack()
            dock2_contents.addWidget(v)
            # v.paint()
        
        dock2_layout = QVBoxLayout()
        dock2_layout.addWidget(dock2_contents)
        dock2_widget = QWidget()
        dock2_widget.setLayout(dock2_layout)
        dock2.setWidget(dock2_widget)

        # Add the dock widgets to the main window
        qTopLayout.addWidget(previewWindow_widget)
        qTopLayout.addWidget(attributesWindow_widget)
        qTopLayout.addWidget(settingsWindow_widget)
        self.top = QDockWidget("<project-name>",self)

        self.index_main.NEW_PROJECT_OPENED.add_handler(self.SetTitle)
        top_qWidget = QWidget()
        top_qWidget.setLayout(qTopLayout)
        self.top.setWidget(top_qWidget)
        self.addDockWidget(Qt.TopDockWidgetArea,self.top)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock2)

        # Set the window title, geometry, and show the main window
        self.setWindowTitle('Video Editor')
        self.setGeometry(300, 300, 1000, 750)
        self.show()

    def SetTitle(self, title: str = "<project-name>"):
        self.top.setWindowTitle(title.split("/")[-1])

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        ss = ""
        for x in FILE_TYPES:
            ss += f"{x[0]} ({x[1]});;"
        file_name, _ = QFileDialog.getOpenFileName(self,"Select a file", "",ss, options=options)
        if file_name:
            self.index_main.NEW_PROJECT_OPENED.fire(file_name)
            with open(file_name, 'r') as file:
                self.attributesWindow_contents.setPlainText(file.read())