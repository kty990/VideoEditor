import tkinter as tk
from tkinter import filedialog
from lib import project
from lib import util

FILE_TYPES = [
    ("Project", f"*{project.PROJECT_FILETYPE}"),
    ("mp4", f"*.mp4")
]

def open_file():
    pass

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create menu bar
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open", command=open_file)
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Add menu bar to window
        self.config(menu=menubar)
        self.title("Video Editor")
        self.title("Video Editor")
        self.geometry("1000x750")
        self.create_widgets()

    def GetOpenFileName(self):
        tmp = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(FILE_TYPES))
        return tmp

    def create_widgets(self):
        # Create PanedWindow
        self.pw_top = tk.PanedWindow(self, orient='horizontal')
        self.pw_bottom = tk.PanedWindow(self, orient='vertical')

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        # Create Top frames
        self.frame_top1 = tk.Frame(self.pw_top, bg='red')
        self.frame_top2 = tk.Frame(self.pw_top, bg='green')
        self.frame_top3 = tk.Frame(self.pw_top, bg='blue')

        self.pw_top.add(self.frame_top1)
        self.pw_top.add(self.frame_top2)
        self.pw_top.add(self.frame_top3)

        # Create Bottom frames
        self.frame_bottom1 = tk.Frame(self.pw_bottom, bg='yellow')
        self.frame_bottom2 = tk.Frame(self.pw_bottom, bg='purple')
        self.frame_bottom3 = tk.Frame(self.pw_bottom, bg='orange')

        self.pw_bottom.add(self.frame_bottom1)
        self.pw_bottom.add(self.frame_bottom2)
        self.pw_bottom.add(self.frame_bottom3)

        # Add PanedWindows to main window
        self.pw_top.pack(fill='both', expand=True, side='top')
        self.pw_bottom.pack(fill='both', expand=True, side='bottom')

        # Set weights
        self.pw_top.paneconfigure(self.frame_top1)
        self.pw_top.paneconfigure(self.frame_top2)
        self.pw_top.paneconfigure(self.frame_top3)

        # Set minimum size of bottom frames to 50% of screen height
        screen_height = self.winfo_screenheight()
        min_height = int(screen_height / 2)
        self.pw_bottom.paneconfigure(self.frame_bottom1, minsize=min_height)
        self.pw_bottom.paneconfigure(self.frame_bottom2, minsize=min_height)
        self.pw_bottom.paneconfigure(self.frame_bottom3, minsize=min_height)

        print("Yes")



    """
    frame - Which frame in the GUI should be updated, in order 1-3 TL -> TR
            followed by 4-6 in order MID -> BOTTOM
    """
    def SetFrame(self, frame: int = 1, new_frame: tk.Widget = None):
        if not isinstance(new_frame, tk.Widget):
            raise TypeError(f"Expected type 'tkinter.Widget', got {type(new_frame)}")
        if not 1 <= frame <= 6:
            raise ValueError(f"Expected frame between 1 and 6, got {frame}")

        if frame == 1:
            self.frame_top1.destroy()
            self.frame_top1 = new_frame
            self.frame_top1.grid(row=0, column=0, sticky="nsew")
            self.pw_top.add(self.frame_top1)
        elif frame == 2:
            self.frame_top2.destroy()
            self.frame_top2 = new_frame
            self.frame_top2.grid(row=0, column=1, sticky="nsew")
            self.pw_top.add(self.frame_top2)
        elif frame == 3:
            self.frame_top3.destroy()
            self.frame_top3 = new_frame
            self.frame_top3.grid(row=0, column=2, sticky="nsew")
            self.pw_top.add(self.frame_top3)
        elif frame == 4:
            self.frame_bottom1.destroy()
            self.frame_bottom1 = new_frame
            self.frame_bottom1.grid(row=0, column=0, sticky="nsew")
            self.pw_bottom.add(self.frame_bottom1)
        elif frame == 5:
            self.frame_bottom2.destroy()
            self.frame_bottom2 = new_frame
            self.frame_bottom2.grid(row=1, column=0, sticky="nsew")
            self.pw_bottom.add(self.frame_bottom2)
        elif frame == 6:
            self.frame_bottom3.destroy()
            self.frame_bottom3 = new_frame
            self.frame_bottom3.grid(row=2, column=0, sticky="nsew")
            self.pw_bottom.add(self.frame_bottom3)

        self.pw_top.paneconfigure(self.frame_top1, minsize=200)
        self.pw_top.paneconfigure(self.frame_top2, minsize=200)
        self.pw_top.paneconfigure(self.frame_top3, minsize=200)
        self.pw_bottom.paneconfigure(self.frame_bottom1, minsize=200)
        self.pw_bottom.paneconfigure(self.frame_bottom2, minsize=200)
        self.pw_bottom.paneconfigure(self.frame_bottom3, minsize=200)
        self.update()