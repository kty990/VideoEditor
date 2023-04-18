import sys
import os

# Get the parent directory of the current file
parent_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'

# Add the parent directory to the system path
sys.path.append(parent_dir)

from lib import display, project, preview

def file_open():
    global proj
    filename = app.GetOpenFileName()
    if filename:
        if proj:
            proj.close()
        try:
            proj = project.Project(filename)
            app.title(f"Video Editor | {filename}")
        except Exception as e:
            print(e)

display.open_file = file_open
app = display.Application()

pWindow = preview.PreviewWindow(app,"")
app.SetFrame(2, pWindow.canvas)

proj = None
file_open()

print(proj)

app.mainloop()