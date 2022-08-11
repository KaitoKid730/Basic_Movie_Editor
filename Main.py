# --------------------------------------------------------------------------------
# ================================================================================
# --------------------------------------------------------------------------------
# Importing the needed libraries
from moviepy.editor import *
import sys
sys.path.append('.\\Formulas')
from Formulas import *			# The formulas which will be used, are kept in a different file
# --------------------------------------------------------------------------------
# ================================================================================
# --------------------------------------------------------------------------------
# Getting all the background videos in a list
print("Getting all the background videos in a list")
Background = []
for x in range(0,11):
	Background.append(VideoFileClip(clipFinder()).without_audio())
print(len(Background))
print("finished - Getting all the background videos in a list")
print("--------------------------------------------------------------------------------")
# --------------------------------------------------------------------------------
# Reading Audio Files
print("Reading Audio Files")
Audio = []
Audio.append(AudioFileClip(".\\Audio\\Intro.mp3"))
for x in range(1,10):
	fileName = ".\\Audio\\"+str(x)+".mp3"
	Audio.append(AudioFileClip(fileName))
Audio.append(AudioFileClip(".\\Audio\\Conc.mp3"))
print(len(Audio))
print("finished - Reading Audio Files")
print("--------------------------------------------------------------------------------")
# --------------------------------------------------------------------------------
# Reading Picture Files
print("Reading Picture Files")
Picture = []
for x in range(1,10):
	fileName = ".\\pics\\"+str(x)+".png"
	Picture.append(ImageClip(fileName))
print(len(Picture))
print("finished - Reading Picture Files")
print("--------------------------------------------------------------------------------")
# --------------------------------------------------------------------------------
# Changing the audio into a videos
print("Changing the audio into a videos")
Section = []
Section.append(matchAudioToBackgroundStartOrEnd(Background[0],Audio[0]))
for x in range(1,len(Audio)-2):
	Section.append(matchAudioToBackground(Background[x],Audio[x],Picture[x-1]))
Section.append(matchAudioToBackgroundStartOrEnd(Background[len(Audio)-1],Audio[len(Audio)-1]))
print("finished - Changing the audio into a videos")
print("--------------------------------------------------------------------------------")
# --------------------------------------------------------------------------------
# Changing the videos into one single video
print("Changing the videos into one single video")
finalVideo = Section[0]
for x in range(1,len(Section)):
	finalVideo = CompositeVideoClip([finalVideo, Section[x]])
print("finished - Changing the videos into one single video")
print("--------------------------------------------------------------------------------")
# --------------------------------------------------------------------------------
# Exporting the file
finalVideo.write_videofile("finalVideo.mp4")