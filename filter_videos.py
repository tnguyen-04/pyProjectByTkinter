import tkinter as tk  
from tkinter import ttk
from font_manager import *  
from subprocess import call  
from video_library import *

window = tk.Tk()
Setup(window, "Video Player", 340, 360)

def showAllVideosOfDirector(event=None):  
    getName = cbb_directorName.get()
    videosOfTheDirector = getVideoOfTheDirector(getName)
    text_filterdVideos.delete(1.0, tk.END)  
    
    for video in videosOfTheDirector:
        getTitle = video.title  
        getDirector = video.director
        getRating = video.rating
        text_filterdVideos.insert(tk.END, f'-{getTitle}\n{getDirector}\n{getRating}\n\n')
    
    totalVideos = len(videosOfTheDirector)
    suffix = "s" if totalVideos>1 else ""
    lbl_videoTotal.config(text=f"Total {totalVideos} video{suffix}")
def backToVideoPlayer():
    window.destroy()
    call(["python", "video_player.py"])

lbl_directorName = tk.Label(window, font="arial 14",text="Director's name")
lbl_directorName.grid(row=0, column=0,pady=10)

directorNameList = getDirectorName()
cbb_directorName = ttk.Combobox(window, values=directorNameList,width=15, font=("Arial", 12))
cbb_directorName.grid(row=0, column=1,pady=(8,0),sticky="we")
cbb_directorName.set("Select a director",)
cbb_directorName.bind("<<ComboboxSelected>>", showAllVideosOfDirector)

text_filterdVideos = tk.Text(window, width=36, height=14, font="arial 12")
text_filterdVideos.grid(row=1,column=0, columnspan=2,padx=(4,0),pady=(0,10))

btn_back = tk.Button(window, text="Back", width=4,font="arial 14", command=backToVideoPlayer)
btn_back.grid(row=2,column=0,padx=(4,0),sticky="we")

lbl_videoTotal = tk.Label(window,text="", font="arial 14")
lbl_videoTotal.grid(row=2, column=1)
window.mainloop()