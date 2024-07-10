import tkinter as tk
from tkinter import messagebox
from font_manager import *
from subprocess import call
from video_library import *

window = tk.Tk()
Setup(window,"Create Video List",735, 400)

def clickedListAllVideos():
    
    videoBox.config(state="normal")
    videoBox.delete("1.0", tk.END)
    
    # Call list_all function to get the list of all videos as a string
    all_videos = list_all()
    
    # Insert the list of all videos into videoBox
    videoBox.insert(tk.END, all_videos)
    
    videoBox.config(state="disabled")
    lbl_listAllVideo.config(text="List Videos button was clicked")
    
videoInPlayList = []
def addToPlayList():
    input_number = ent_enterNumber.get().strip()
    ent_enterNumber.delete(0, tk.END)
    box_addPlaylist.config(state="normal")
    
    if input_number.isdigit() and int(input_number) > 0:
        number = int(input_number)
        videoInPlayList.append(int(number))
        getPLays = get_play_count(number)
        getTitle = get_name(number)
        
        if  increment_play_count is not None and getTitle is not None and getPLays is not None:
            prefixNumber = "0" if number < 9 else ""
            box_addPlaylist.insert(tk.END, f"{prefixNumber}{number}.{getTitle} || played:{getPLays}\n")
            
        else:
            messagebox.showerror("Error", "Video not found")
    
    else:
        messagebox.showerror("Error", "Please enter a valid video number.")
    box_addPlaylist.config(state="disabled") 

def playTheList():
    box_addPlaylist.config(state="normal")
    box_addPlaylist.delete("1.0", tk.END) 
    
    for videoNumber in videoInPlayList:
        getTitle = get_name(videoNumber)
        incrementPLays = increment_play_count(videoNumber)
        if incrementPLays is not None:  
            prefixNumber = "0" if videoNumber < 9 else ""
            box_addPlaylist.insert(tk.END, f"{prefixNumber}{videoNumber}.{getTitle} || played:{incrementPLays}\n")
    
    box_addPlaylist.config(state="disabled")

def resetPLaylist():
    box_addPlaylist.config(state="normal")
    box_addPlaylist.delete("1.0", tk.END) 
    
    for videoNumber in videoInPlayList:
        reset(videoNumber)

def backToVideoPlayer():
    window.destroy()
    call(["python", "video_player.py"])

btn_back = tk.Button(window, text='Back', font="arial 14", command=backToVideoPlayer)
btn_back.grid(row=0, column=0,pady=10,padx=(5,0))

btn_ListAllVideos = tk.Button(window, text="List All Videos", font="arial 14", command=clickedListAllVideos)
btn_ListAllVideos.grid(row=0, column=1,pady=10)

lbl_enterVideoNumber = tk.Label(window, text="Enter Video Number", font="arial 14")
lbl_enterVideoNumber.grid(row=0, column=2,pady=10)

ent_enterNumber = tk.Entry(window, font="arial 14", width="4")
ent_enterNumber.grid(row=0, column=3,pady=10)

btn_addToPLaylist = tk.Button(window, text="Add to Playlist", font="arial 14",command=addToPlayList)
btn_addToPLaylist.grid(row=0, column=4,pady=10,padx=(10,10))

btn_resetPlaylist = tk.Button(window, text="Reset", font="arial 14", command=resetPLaylist)
btn_resetPlaylist.grid(row=0, column=5,pady=10)

videoBox = tk.Text(window, height=18, width=60, state="disabled")
videoBox.grid(row=1, column=0, columnspan=4, rowspan=3,padx=(5,0))

box_addPlaylist = tk.Text(window, height=14, width=28,wrap=tk.WORD)
box_addPlaylist.grid(row=1, column=4,columnspan=2, rowspan=2,padx=(10,0), pady=(0,10))

btn_playPLaylist = tk.Button(window, text="Play Number", font="arial 14",width=12,command=playTheList)
btn_playPLaylist.grid(row=3, column=4,columnspan=2,padx=(10,0))

lbl_listAllVideo = tk.Label(window, text="", font="arial 14")
lbl_listAllVideo.grid(row=4, column=0,columnspan=2,sticky="w")

window.mainloop()
