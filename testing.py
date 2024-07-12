import pytest 
from check_videos import *
from create_video_list import *
from filter_videos import *
from update_videos import *
from video_library import *

# testing get title
def test_get_name():
    assert get_name(1) == "Tom and Jerry" #best
    assert get_name(70) == "The Martian" #average
    assert get_name(131) == None #worst
    
# testing get director
def test_get_director():
    assert get_director(1) == "Fred Quimby" #best
    assert get_director(70) == "Ridley Scott"#average
    assert get_director(131) == None #worst
    
    
