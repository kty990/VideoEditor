import tkinter as tk
from tkinter import filedialog

from lib import project

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

        try:
            # Create the main window
            self.configure(bg='black')
            self.title("Video Editor")
            self.geometry("1000x750")

            # Create the top level frames
            frame_top = tk.Frame(self, bg='black')
            frame_top.pack(side='top', fill='both', expand=True)

            frame1 = tk.Frame(frame_top, bg='white', bd=2, relief='groove')
            frame1.pack(side='left', fill='both', expand=True)
            label1 = tk.Label(frame1, text='Frame 1', font=('Arial', 16), fg='black')
            label1.pack(pady=10)

            frame2 = tk.Frame(frame_top, bg='white', bd=2, relief='groove')
            frame2.pack(side='left', fill='both', expand=True)
            label2 = tk.Label(frame2, text='Frame 2', font=('Arial', 16), fg='black')
            label2.pack(pady=10)

            frame3 = tk.Frame(frame_top, bg='white', bd=2, relief='groove')
            frame3.pack(side='left', fill='both', expand=True)
            label3 = tk.Label(frame3, text='Frame 3', font=('Arial', 16), fg='black')
            label3.pack(pady=10)

            # Create the bottom level frame
            frame_bottom = tk.Frame(self, bg='black', bd=2, relief='groove')
            frame_bottom.pack(side='bottom', fill='both', expand=True)

            # Create the nested frames in the bottom level frame
            frame4 = tk.Frame(frame_bottom, bg='white')
            frame4.pack(side='top', fill='both', expand=True)
            label4 = tk.Label(frame4, text='Frame 4', font=('Arial', 16), fg='black')
            label4.pack(pady=10)

            frame5 = tk.Frame(frame_bottom, bg='white', bd=2, relief='groove')
            frame5.pack(side='top', fill='both', expand=True)
            label5 = tk.Label(frame5, text='Frame 5', font=('Arial', 16), fg='black')
            label5.pack(pady=10)

            frame6 = tk.Frame(frame_bottom, bg='white')
            frame6.pack(side='top', fill='both', expand=True)
            label6 = tk.Label(frame6, text='Frame 6', font=('Arial', 16), fg='black')
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
                    frame_top.configure(width=current_width, height=current_height / 2)
                    frame_bottom.configure(width=current_width, height=current_height / 2)
                    frame1.configure(width=frame1_width, height=frame1_height)
                    frame2.configure(width=frame2_width, height=frame2_height)
                    frame3.configure(width=frame3_width, height=frame3_height)
                    frame4.configure(height=frame4_height)
                    frame5.configure(height=frame5_height)
                    frame6.configure(height=frame6_height)

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