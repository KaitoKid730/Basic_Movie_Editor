import random
from moviepy.editor import *
def clipFinder():
	num = random.randint(1,9)
	fileName = ".\\Loop Videos\\"+str(num)+".mp4"
	return fileName

# Changing the audio into a video
def matchAudioToBackground(video,audio,pic):
	# Getting durations of audio and videos
	lengthOfAudio = audio.duration
	lengthOfVideo = video.duration

	# Getting how many times the video will be repeated
	numberOfTimesToBeRepeated = lengthOfAudio//lengthOfVideo
	extraDuration = lengthOfAudio - lengthOfVideo*numberOfTimesToBeRepeated

	# repeating the video to the number of times
	finalVideo = video
	for x in range(0,int(numberOfTimesToBeRepeated)):
		finalVideo = concatenate_videoclips([finalVideo,video])

	# Adding the extra duration that is needed
	video.subclip(0,extraDuration)
	finalVideo = concatenate_videoclips([finalVideo,video])

	# Adding the picture in the video
	pic.set_start(0).set_duration(lengthOfAudio).set_pos(("center","center")).resize(height=720)
	finalVideo = CompositeVideoClip([finalVideo, pic])
	finalVideo = finalVideo.set_audio(audio)
	return finalVideo

def matchAudioToBackgroundStartOrEnd(video,audio):
	# Getting durations of audio and videos
	lengthOfAudio = audio.duration
	lengthOfVideo = video.duration

	# Getting how many times the video will be repeated
	numberOfTimesToBeRepeated = lengthOfAudio//lengthOfVideo
	extraDuration = lengthOfAudio - lengthOfVideo*numberOfTimesToBeRepeated

	# repeating the video to the number of times
	finalVideo = video
	for x in range(0,int(numberOfTimesToBeRepeated)):
		finalVideo = concatenate_videoclips([finalVideo,video])

	# Adding the extra duration that is needed
	video.subclip(0,extraDuration)
	finalVideo = concatenate_videoclips([finalVideo,video])
	finalVideo = finalVideo.set_audio(audio)
	return finalVideo