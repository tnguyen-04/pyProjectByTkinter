import tkinter as tk
from tkinter import messagebox
from font_manager import *
from subprocess import call
from video_library import *
window = tk.Tk()
Setup(window,"Check Videos",700, 400)

def clickedListAllVideos():
    
    videoBox.config(state="normal")
    videoBox.delete("1.0", tk.END)
    
    # Call list_all function to get the list of all videos as a string
    all_videos = list_all()
    
    # Insert the list of all videos into videoBox
    videoBox.insert(tk.END, all_videos)
    
    videoBox.config(state="disabled")
    lbl_listAllVideo.config(text="List Videos button was clicked")

def checkVideos():
    input_number = ent_enterNumber.get()
    ent_enterNumber.delete(0, tk.END)
    box_checkVideos.config(state="normal")
    box_checkVideos.delete("1.0", tk.END)
    
    if input_number.isdigit() and int(input_number) > 0:
        number = int(input_number)
        
        getTitle = get_name(number)
        getDirector = get_director(number)
        getRating = get_rating(number)
        getPlays = get_play_count(number)
        
        if getTitle is not None and getDirector is not None and getRating is not None and getPlays is not None:
            box_checkVideos.insert(tk.END, f"Title: {getTitle}\n")
            box_checkVideos.insert(tk.END, f"Director: {getDirector}\n")
            box_checkVideos.insert(tk.END, f"Rating: {getRating}\n")
            box_checkVideos.insert(tk.END, f"Plays: {getPlays}\n")
        else:
            messagebox.showerror("Error", "Video not found")
    
    else:
        messagebox.showerror("Error", "Please enter a valid video number.")
    box_checkVideos.config(state="disabled")
    
def backToVideoPlayer():
    window.destroy()
    call(["python", "video_player.py"])

btn_back = tk.Button(window, text='Back', font="arial 14", command=backToVideoPlayer)
btn_back.grid(row=0, column=0, padx=(10, 10), pady=10,sticky="w")

# Button to list all videos
btn_ListAllVideos = tk.Button(window, text="List All Videos", font="arial 14", command=clickedListAllVideos)
btn_ListAllVideos.grid(row=0, column=1, padx=(10, 10), pady=10)


# Label for entering video number
lbl_enterVideoNumber = tk.Label(window, text="Enter Video Number", font="arial 14")
lbl_enterVideoNumber.grid(row=0,column=2)

# Entry for entering video number
ent_enterNumber = tk.Entry(window, font="arial 14", width="4")
ent_enterNumber.grid(row=0,column=3)

# Button to check a specific video
btn_checkVideo = tk.Button(window, text="Check Video", font="arial 14", command=checkVideos)
btn_checkVideo.grid(row=0, column=4, padx=(10, 10), pady=10)

# Text box for displaying videos
videoBox = tk.Text(window, height=18, width=60)
videoBox.grid(row=1, column=0, columnspan=4, padx=(5, 15), pady=(0, 10), sticky="w")

# Text box for check videos
box_checkVideos = tk.Text(window, height=5, width=22, wrap=tk.WORD)
box_checkVideos.grid(row=1, column=4, sticky="n")

# Label below the videoBox
lbl_listAllVideo = tk.Label(window, text="", font="arial 14")
lbl_listAllVideo.grid(row=2, column=0, padx=(5, 0),columnspan=2,sticky="w")

window.mainloop()

