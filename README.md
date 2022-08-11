# Basic_Movie_Editor
In this repository, I will be making a very simple movie editor. The least of my concerns is the GUI, so I am not sure it will help someone who doesn't know coding. However, it will benefit people who want to learn how to code by learning from whatever I am able to share in it.<br>

The main motivation for making this program is to learn how to use MoviePy mostly. So I will be trying my best to explain what the code does for everyone who wants to learn about MoviePy and how to use it.<br><br>

Disclaimer:
-------------------
This program is horribly made. Because the goal of this program is to share the information that I gathered in editing a video using MoviePy. So don't expect this program to replace your fancy video editing software.

Explanation:
-------------------
Here I will be going through each section so it will help you understand what the code is doing. So that it will help you understand what is written: <br>
        
    Background = []
    for x in range(0,11):
      Background.append(VideoFileClip(clipFinder()).without_audio())
    print(len(Background))

In the above section, I am just reading the list of videos from a different folder. Then I am adding those videos without audio so I can add the audio later on.

    Audio = []
    Audio.append(AudioFileClip(".\\Audio\\Intro.mp3"))
    for x in range(1,10):
        fileName = ".\\Audio\\"+str(x)+".mp3"
        Audio.append(AudioFileClip(fileName))
    Audio.append(AudioFileClip(".\\Audio\\Conc.mp3"))

In the above section, I am just reading the audio files. It just so happens that the audio files are named Intro, Conc, and the numbers between 1 and 10.

    Picture = []
    for x in range(1,10):
        fileName = ".\\pics\\"+str(x)+".png"
        Picture.append(ImageClip(fileName))
        
In the above section, I am just reading the pictures into a list. <br/>
You will notice that for the audio, pictures, and videos, I am saving them in an array. I am just doing it because it makes life easier while interacting with it.

    Section = []
    Section.append(matchAudioToBackgroundStartOrEnd(Background[0],Audio[0]))
    for x in range(1,len(Audio)-2):
        Section.append(matchAudioToBackground(Background[x],Audio[x],Picture[x-1]))
    Section.append(matchAudioToBackgroundStartOrEnd(Background[len(Audio)-1],Audio[len(Audio)-1]))
    
In the above section, I am just matching the first audio file to the background while making sure that the video will keep on repeating until the first audio is finished. And in the loop, you can see that I am just adding 1 extra step, which is adding a picture to the center of the video. And for the conclusion, I am doing the same thing as in the 1st video.

    finalVideo = Section[0]
    for x in range(1,len(Section)):
        finalVideo = CompositeVideoClip([finalVideo, Section[x]])

In the above section, I am just adding all the sections together into one file. So, I can just export the entire video once.
