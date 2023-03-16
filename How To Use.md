# ***YT-Audio-Snipper***
This is a Python script that will download only a selected portion of a Youtube video's audio based on the start and end times that you provide.

# Installation

This uses ***ffmpeg*** & ***pytube***, so make sure to install both before running.

Here is the link to download ffmpeg: https://www.gyan.dev/ffmpeg/builds/

Make sure to extract the ffmpeg .zip to a safe spot on your PC, like in your Program Files.

You'll have to take the .exe files found in the bin folder and add them to your system path which can be done by searching for "System variables" in the start menu and clicking on "Edit the system environment variables". From there, in the advanced tab, click on "Environment Variables" in the bottom right. Then, in the "System Variables" section, scroll down until you see "path" and click "Edit". Now, click "new" and add the file's path and click "Okay".

Here's what that might look like:

```C:\Program Files\ffmpeg-2023-03-05-git-912ac82a3c-essentials_build\bin\ffmpeg.exe```

```C:\Program Files\ffmpeg-2023-03-05-git-912ac82a3c-essentials_build\bin\ffplay.exe```

```C:\Program Files\fmpeg-2023-03-05-git-912ac82a3c-essentials_build\bin\ffprobe.exe```

To install pytube, open a terminal window and enter ```pip install pytube3```.
You need to have pip installed on your PC, which should be included when installing Python on your PC.

Here's a link to install Python if you don't already have it: https://www.python.org/downloads/

# Usage
To use the script, open the .py file with a text editor of your choosing and find this line at the end of the script:
```download_audio('ENTER_THE_YOUTUBE_URL_HERE', 'START_TIME', 'END_TIME')```

Replace ```'ENTER_THE_YOUTUBE_URL_HERE'``` with the URL to the youtube video and replace ```'START_TIME'``` & ```'END_TIME'``` with the start and end times in this format: ***hour:minute:second***

Make sure to not remove the apostrophes.

It should look something like this: ```download_audio('https://www.youtube.com/watch?v=6xnG2XQXnc0', '00:00:57', '00:01:29')```

Once done, save the .py file and run it.

That's it! You have now downloaded an audio snippet of a Youtube video with the start and end times you provided.

Enjoy!
