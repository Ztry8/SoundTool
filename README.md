# SoundTool
## Simple and fast script to normalize SFX and music for games


### About
Sound effects (SFX) can sometimes be recorded at different volumes.  
For example, the sound of an explosion is usually louder than the sound of footsteps.  
This program adjusts all sounds to the same volume.  

The music folder and SFX folder paths are input.  
The files in the folders have a .data extension, but the data inside is in .ogg/.wav/.flac format.  
The script puts all the files on the same volume level and saves the data as a .flac file,
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
Enter SFX folder path: sounds_orig
Enter output folder for SFX: sounds

Enter Music folder path: music_orig
Enter output folder for Music: music

Using volume targets:
Sound Effects (SFX): -18.0 dBFS
Music: -23.0 dBFS

Processing SFX...
Detected WAV: melee_attack1.data
Processed: melee_attack1.data (-13.3dB -> -18.0dB)
Detected OGG: door_open.data
Processed: door_open.data (-22.7dB -> -18.8dB)

Processing music...
Detected OGG: day.data
Processed: day.data (-41.3dB -> -23.0dB)
Detected OGG: night.data
Processed: night.data (-40.9dB -> -23.0dB)

SFX: 2 files processed
Music tracks: 2 files processed
```
