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


### Installation

#### Windows
[Install ffmpeg](https://ffmpeg.org/download.html#build-windows) and [install python](https://www.python.org/downloads/windows/).   
After that:
```
pip install pydub
```

#### Linux
Firstly, install [ffmpeg](https://ffmpeg.org/):   
For Debian-based:
```
sudo apt install ffmpeg
```
For Arch-based
```
sudo pacman -S ffmpeg
```
For RHEL-based (Note: you need to enable [EPEL](https://docs.fedoraproject.org/en-US/epel/) and [RPM Fusion](https://docs.fedoraproject.org/en-US/quick-docs/rpmfusion-setup/) first):
```
sudo dnf install ffmpeg ffmpeg-devel
```

After that install pip, in most cases, you can install like this:
```
pip3 install pydub
```

However in Debian 12 (which I used), there is no `pip` installed by default,   
and installing Python modules causes errors.  
I recommend installing the dependency using the command:   
```
sudo apt install python3-pydub
```

#### MacOS

For MacOS (in example python version 3.6 but you can set your own): 
```
sudo port install ffmpeg
sudo port install python36
sudo port install py36-pip
sudo port select --set python3 python36
sudo port select --set pip3 pip36
```

### Usage
```
python3 main.py
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
