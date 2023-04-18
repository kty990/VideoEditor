import tkinter as tk

def DeepCopyWidget(widget):
    # Create a new widget of the same type and with the same options
    widget_copy = widget.__class__(widget.master, **widget.config())

    # Copy the widget's text or image
    if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
        widget_copy.configure(text=widget.cget('text'))
    # elif isinstance(widget, tk.Canvas):
    #     widget_copy.create_image(0, 0, image=widget.create_image(0, 0, image=widget.image, anchor='nw'), anchor='nw')

    widget.option_add("*visual","TrueColor")

    # Copy the widget's children
    for child_widget in widget.winfo_children():
        child_copy = DeepCopyWidget(child_widget)
        child_copy#.pack_forget()
        widget_copy#.pack_forget()
        child_copy.pack(widget_copy, side='top', expand=True, fill='both')

    return widget_copy
