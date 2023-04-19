import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QDockWidget, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt

# Get the parent directory of the current file
parent_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'

# Add the parent directory to the system path
sys.path.append(parent_dir)

from lib import project

FILE_TYPES = [
    ("Project", f"*{project.PROJECT_FILETYPE}"),
    ("All Files", f"*")
]

class Application(QMainWindow):

    def __init__(self, app):
        super().__init__()

        self.app = app

        self.initUI()

    def initUI(self):

        # Create a menu bar and add a "Open" action to it
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Create a QTextEdit widget
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # Create a QDockWidget with a QVBoxLayout
        dock1 = QDockWidget("Dockable", self)
        dock1.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        dock1_contents = QTextEdit()
        dock1_layout = QVBoxLayout()
        dock1_layout.addWidget(dock1_contents)
        dock1_widget = QWidget()
        dock1_widget.setLayout(dock1_layout)
        dock1.setWidget(dock1_widget)

        # Create another QDockWidget with a QVBoxLayout
        dock2 = QDockWidget("Dockable 2", self)
        dock2.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        dock2_contents = QTextEdit()
        dock2_layout = QVBoxLayout()
        dock2_layout.addWidget(dock2_contents)
        dock2_widget = QWidget()
        dock2_widget.setLayout(dock2_layout)
        dock2.setWidget(dock2_widget)

        # Add the dock widgets to the main window
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        # Set the window title, geometry, and show the main window
        self.setWindowTitle('Video Editor')
        self.setGeometry(300, 300, 1000, 750)
        self.show()

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        ss = ""
        for x in FILE_TYPES:
            ss += f"{x[0]} ({x[1]});;"
        file_name, _ = QFileDialog.getOpenFileName(self,"Select a file", "",ss, options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.centralWidget().setPlainText(file.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application(app)
    sys.exit(app.exec_())
