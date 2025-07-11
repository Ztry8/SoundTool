# SoundTool
## Simple and fast script to normalize SFX and music for games


### About
Sound effects (SFX) can sometimes be recorded at different volumes.  
For example, the sound of an explosion is usually louder than the sound of footsteps.  
This program adjusts all sounds to the same volume.  

The music folder and SFX folder paths are input.  
The files in the folders have a .data extension, but the data inside is in .ogg or .wav format.  
The script puts all the files on the same volume level and saves the data as a .wav file.
but in .data file format.

(Processed sounds usually stay the same quality,   
but in some cases, there might be a small loss of quality)

(The .data file extension is a requirement of the my game engine)


### Usage

#### Linux
[Install ffmpeg](https://ffmpeg.org/download.html)    
`(sudo) apt install ffmpeg` e.g. for Debian/Ubuntu


In Debian 12 (which I use), there is no `pip` installed by default,   
and installing Python modules causes errors.  
I recommend installing the dependency using the command:   
`(sudo) apt install python3-pydub`

For others, you can use the command
`pip3 install pydub`

And run: `python3 tool.py`

#### Windows/MacOS
[Install ffmpeg](https://ffmpeg.org/download.html).   
For MacOS: `brew install ffmpeg`

```
pip install pydub
python tool.py
```

### Output
```
==================================================
AUDIO NORMALIZATION TOOL
==================================================

Enter SFX folder path: sounds
Enter output folder for SFX: done_sounds

Enter Music folder path: music
Enter output folder for Music: done_music

Using volume targets:
Sound Effects (SFX): -18.0 dBFS
Music: -23.0 dBFS

==============================
PROCESSING SOUND EFFECTS
==============================
Processed: melee_attack1.data (-13.3dB -> -18.0dB)
Processed: melee_attack2.data (-14.4dB -> -18.0dB)
Processed: melee_attack3.data (-17.6dB -> -18.0dB)

==============================
PROCESSING MUSIC
==============================
Processed: day.data (-41.3dB -> -23.0dB)
Processed: night.data (-40.9dB -> -23.0dB)

==================================================
PROCESSING COMPLETE!
Sound Effects: 3 files
Music tracks: 2 files
==================================================
```
