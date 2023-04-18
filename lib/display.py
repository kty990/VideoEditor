import tkinter as tk
from tkinter import filedialog

from lib import project

FILE_TYPES = [
    ("Project", f"*{project.PROJECT_FILETYPE}"),
    ("mp4", f"*.mp4")
]

#This is empty for a reason
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

        try:
            # Create the main window
            self.configure(bg='black')
            self.title("Video Editor")
            self.geometry("1000x750")

            # Create the top level frames
            self.frame_top = tk.Frame(self, bg='black')
            self.frame_top.pack(side='top', fill='both', expand=True)

            self.frame1 = tk.Frame(self.frame_top, bg='white', bd=2, relief='groove')
            self.frame1.pack(side='left', fill='both', expand=True)
            label1 = tk.Label(self.frame1, text='Frame 1', font=('Arial', 16), fg='black')
            label1.pack(pady=10)

            self.frame2 = tk.Frame(self.frame_top, bg='white', bd=2, relief='groove')
            self.frame2.pack(side='left', fill='both', expand=True)
            label2 = tk.Label(self.frame2, text='Frame 2', font=('Arial', 16), fg='black')
            label2.pack(pady=10)

            self.frame3 = tk.Frame(self.frame_top, bg='white', bd=2, relief='groove')
            self.frame3.pack(side='left', fill='both', expand=True)
            label3 = tk.Label(self.frame3, text='Frame 3', font=('Arial', 16), fg='black')
            label3.pack(pady=10)

            # Create the bottom level frame
            self.frame_bottom = tk.Frame(self, bg='black', bd=2, relief='groove')
            self.frame_bottom.pack(side='bottom', fill='both', expand=True)

            # Create the nested frames in the bottom level frame
            self.frame4 = tk.Frame(self.frame_bottom, bg='white')
            self.frame4.pack(side='top', fill='both', expand=True)
            label4 = tk.Label(self.rame4, text='Frame 4', font=('Arial', 16), fg='black')
            label4.pack(pady=10)

            self.frame5 = tk.Frame(self.frame_bottom, bg='white', bd=2, relief='groove')
            self.frame5.pack(side='top', fill='both', expand=True)
            label5 = tk.Label(self.frame5, text='Frame 5', font=('Arial', 16), fg='black')
            label5.pack(pady=10)

            self.frame6 = tk.Frame(self.frame_bottom, bg='white')
            self.frame6.pack(side='top', fill='both', expand=True)
            label6 = tk.Label(self.frame6, text='Frame 6', font=('Arial', 16), fg='black')
            label6.pack(pady=10)


            prev_width = None
            prev_height = None
            update_id = None
            updating = False

            def on_window_resize(event):
                global prev_width, prev_height, update_id
                global updating
                print("setting window size")
                if updating:
                    return
                updating = True
                # Get the current width and height
                current_width = event.width
                current_height = event.height

                # Check if the width or height has changed since the last time this function was called
                if prev_width != current_width or prev_height != current_height:
                    # Update the previous width and height
                    prev_width = current_width
                    prev_height = current_height

                    # Cancel the previously scheduled update, if any
                    if update_id is not None:
                        self.after_cancel(update_id)

                    # Calculate the new frame widths and heights
                    frame1_width = current_width / 3
                    frame2_width = current_width / 3
                    frame3_width = current_width / 3
                    frame1_height = current_height / 2
                    frame2_height = current_height / 2
                    frame3_height = current_height / 2
                    frame4_height = current_height / 6
                    frame5_height = current_height / 6
                    frame6_height = current_height / 6

                    # Update the frame configurations
                    self.frame_top.configure(width=current_width, height=current_height / 2)
                    self.frame_bottom.configure(width=current_width, height=current_height / 2)
                    self.frame1.configure(width=frame1_width, height=frame1_height)
                    self.frame2.configure(width=frame2_width, height=frame2_height)
                    self.frame3.configure(width=frame3_width, height=frame3_height)
                    self.frame4.configure(height=frame4_height)
                    self.frame5.configure(height=frame5_height)
                    self.frame6.configure(height=frame6_height)

                    # Update the label font size
                    label_font_size = int(frame1_width / 20)
                    label1.configure(font=('Arial', label_font_size))
                    label2.configure(font=('Arial', label_font_size))
                    label3.configure(font=('Arial', label_font_size))
                    label4.configure(font=('Arial', label_font_size))
                    label5.configure(font=('Arial', label_font_size))
                    label6.configure(font=('Arial', label_font_size))

                    # Schedule a new update in 100 milliseconds
                    update_id = self.after(1000, reset_update_flag)
                updating = False

                    
                def reset_update_flag():
                    global update_id
                    update_id = None


                self.bind("<Configure>", on_window_resize)
        except:
            print("An exception occured.")

    def GetOpenFileName(self):
        tmp = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(FILE_TYPES))
        return tmp
    
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
            self.frame1 = new_frame
            self.frame1.pack(side='left', fill='both', expand=True)
        elif frame == 2:
            self.frame2 = new_frame
            self.frame2.pack(side='left', fill='both', expand=True)
        elif frame == 3:
            self.frame3 = new_frame
            self.frame3.pack(side='left', fill='both', expand=True)
        elif frame == 4:
            self.frame4 = new_frame
            self.frame4.pack(side='top', fill='both', expand=True)
        elif frame == 5:
            self.frame5 = new_frame
            self.frame5.pack(side='top', fill='both', expand=True)
        elif frame == 6:
            self.frame6 = new_frame
            self.frame6.pack(side='top', fill='both', expand=True)
        


