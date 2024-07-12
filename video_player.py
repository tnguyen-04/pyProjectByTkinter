import tkinter as tk
from font_manager import *
from subprocess import call

window = tk.Tk()
Setup(window, "Video Player", 470, 150)

def checkVideos():
    window.destroy()
    call(["python", "check_videos.py"])

def createVideo():
    window.destroy()
    call(["python", "create_video_list.py"])

def updateVideo():
    window.destroy()
    call(["python", "update_videos.py"])

def filterVideos():
    window.destroy()
    call(["python", "filter_videos.py"])

lbl = tk.Label(window, text="Select an option by clicking one of the buttons below", font=("Arial", 14))
lbl.grid(row=0, column=0, columnspan=3, pady=10)

btn_check = tk.Button(window, text="Check Videos", font=("Arial", 14), command=checkVideos)
btn_check.grid(row=1, column=0, padx=5, pady=5)

btn_create = tk.Button(window, text="Create Video List", font=("Arial", 14), command=createVideo)
btn_create.grid(row=1, column=1, padx=5, pady=5)

btn_update = tk.Button(window, text="Update Videos", font=("Arial", 14), command=updateVideo)
btn_update.grid(row=1, column=2, padx=5, pady=5)

btn_filter = tk.Button(window, text="Filter Videos By Director's Name",width=35, font=("Arial", 14), command=filterVideos, borderwidth=3)
btn_filter.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
