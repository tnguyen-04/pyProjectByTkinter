import tkinter as tk
from tkinter import messagebox
from font_manager import *
from subprocess import call
from video_library import *

window = tk.Tk()
Setup(window, "Update Videos", 735, 412)

def clickedListAllVideos():
    
    videoBox.config(state="normal")
    videoBox.delete("1.0", tk.END)
    
    
    result = ""
    for idx, video in enumerate(video_list):
        prefixNumber = "0" if idx < 9 else ""
        result += f"{prefixNumber}{video.number} {video.title} - {video.director} || Rating:{video.rating}\n"
    
    videoBox.insert(tk.END, result)
    
    videoBox.config(state="disabled")
    lbl_listAllVideo.config(text="List Videos button was clicked")

def updateNewRating():
    input_number =ent_enterNumber.get().strip()
    new_Rating = ent_enterRating.get().strip()
    ent_enterNumber.delete(0, tk.END)
    box_updateVideos.config(state="normal")
    
    if input_number.isdigit() and int(input_number) > 0 and new_Rating.isdigit() and float(new_Rating)>0 and float(new_Rating)<10:
        number = int(input_number)
        getTitle = get_name(number)
        getDirector = get_director(number)
        newRating = updateRating(number, new_Rating)
        getPlays = get_play_count(number)
        
        if  getTitle is not None and getDirector is not None and getPlays is not None and newRating is not None:
            box_updateVideos.insert(tk.END, f"Title: {getTitle}\nDirector: {getDirector}\nRating: {newRating}\nPlays: {getPlays}")
        else:
            messagebox.showerror("Error", "Video not found")
    else:
        messagebox.showerror("Error", "Please enter a valid video number.")
    box_updateVideos.config(state="disabled")
    
def backToVideoPlayer():
    window.destroy()
    call(["python", "video_player.py"])

# Text box for displaying videos
videoBox = tk.Text(window, height=22, width=58, state="disabled")
videoBox.grid(row=0, column=0, rowspan=5, columnspan=2, padx=(5,10),pady=(10,0),sticky='nsew')

# Button to list all videos
btn_ListAllVideos = tk.Button(window, text="List All Videos", font="arial 14",width=20, command=clickedListAllVideos)
btn_ListAllVideos.grid(row=0, column=2, columnspan=2,padx=(5,0),pady=(10,0), sticky='nw')


# Label for entering video number
lbl_enterVideoNumber = tk.Label(window, text="Enter Video Number", font="arial 14")
lbl_enterVideoNumber.grid(row=1, column=2, padx=(5,0),sticky='new')


# Entry for entering video number
ent_enterNumber = tk.Entry(window, font="arial 14", width=3)
ent_enterNumber.grid(row=1, column=3,padx=(5,0), sticky='w')

# Label for entering new rating
lbl_enterRating = tk.Label(window,  text="Enter New Rating", font="arial 14")
lbl_enterRating.grid(row=2, column=2,padx=(5,0), sticky='w')

# Entry for entering new rating
ent_enterRating = tk.Entry(window, font="arial 14", width=3)
ent_enterRating.grid(row=2, column=3,padx=(5,10), sticky='w')

btn_updateRating = tk.Button(window, text="Update Rating",width=20,font="arial 14", command=updateNewRating)
btn_updateRating.grid(row=3, column=2, columnspan=2,padx=(5,0), sticky='w')

# Text box for check videos
box_updateVideos = tk.Text(window, height=5, width=21, wrap=tk.WORD, font="arial 14"  )
box_updateVideos.grid(row=4, column=2, columnspan=2,padx=(5,0), sticky='w')
# Label below the videoBox
lbl_listAllVideo = tk.Label(window, text="",font="arial 14")
lbl_listAllVideo.grid(row=5, column=0, columnspan=2, sticky='w')

btn_back = tk.Button(window, text="Back", width=4,font="arial 14", command=backToVideoPlayer)
btn_back.grid(row=5, column=3,padx=(0,50),sticky='w')

window.mainloop()
