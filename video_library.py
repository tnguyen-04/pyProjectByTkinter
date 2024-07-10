import csv

class Video:
    def __init__(self, number, title, director, rating,plays):
        self.number = number
        self.title = title
        self.director = director
        self.rating = rating
        self.plays = plays

video_list = []

with open('videoStorage.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Bỏ qua dòng tiêu đề
    for row in reader:
        if len(row)>=5:
            video_list.append(Video(int(row[0]), row[1], row[2],float(row[3]), int(row[4])))

video_list.sort(key=lambda x: x.number)        


def list_all():
    result = ""
    for idx, video in enumerate(video_list):
        prefixNumber = "0" if idx < 9 else ""
        result += f"{prefixNumber}{video.number} {video.title} - {video.director}\n"
    return result

#===========================================================================
def binary_search(number):

    low = 0
    high = len(video_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if video_list[mid].number == number:
            return True 
        elif video_list[mid].number < number:
            low = mid + 1
        else:
            high = mid - 1
    return None

def get_name( number):
    if binary_search(number):
        return video_list[number - 1].title
    else:
        return None
    
def get_number( number):
    if binary_search(number):
        return video_list[number - 1].number
    else:
        return None

def get_director( number):
    if binary_search(number):
        return video_list[number - 1].director
    else:
        return None

def get_rating( number):
    if binary_search(number):
        return video_list[number - 1].rating
    else:
        return None

def get_play_count( number):
    if binary_search(number):
        return video_list[number - 1].plays
    else:
        return None

def updatePlayCountToCsv(number, playIncrement):
    rows = []
    with open('videoStorage.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            rows.append(row)
  
    
    for row in rows:
        if row[0] == str(number):  
            row[4] = str(playIncrement)  
            break
    
    with open('videoStorage.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def increment_play_count(number):
    
    if binary_search(number) is not None:
        video_list[number-1].plays += 1
        updatePlayCountToCsv(number, video_list[number-1].plays)
        return video_list[number - 1].plays
    else:
        return None
        
def reset(number):       
    if binary_search(number) is not None:
        video_list[number-1].plays = 0
        updatePlayCountToCsv(number, video_list[number-1].plays)
        return video_list[number - 1].plays
    else:
        return None  

def updateRatingToCsv(videoNumber, newRating):
    rows = []
    with open('videoStorage.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            rows.append(row)

    for row in rows:
        if row[0] == str(videoNumber):  
            row[3] = str(newRating)  
            break
    
    with open('videoStorage.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def updateRating(videoNumber, newRating):
    if binary_search(videoNumber) is not None:
        video_list[videoNumber-1].rating = newRating
        updateRatingToCsv(videoNumber,video_list[videoNumber-1].rating)
        return video_list[videoNumber - 1].rating
    else:
        return None  


def getDirectorName():
    directorName = set()
    with open('videoStorage.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            directorName.add(row[2])
        sortedDirectorName = list(sorted(directorName))
        return sortedDirectorName
    
def getVideoOfTheDirector(directorName):
    directorVideos = []
    with open('videoStorage.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[2] == directorName:
                directorVideos.append(Video(int(row[0]), row[1], row[2],float(row[3]), int(row[4])))
        return directorVideos