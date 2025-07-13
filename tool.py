import os
import sys
from pydub import AudioSegment
from pydub.effects import normalize
from io import BytesIO

def process_folder(input_path, output_path, target_dBFS):
    if not os.path.exists(input_path):
        print(f"ERROR: Input folder not found: {input_path}")
        return -1
        
    os.makedirs(output_path, exist_ok=True)
    processed = 0
    
    for filename in os.listdir(input_path):
        if not filename.endswith('.data'):
            continue
            
        full_input = os.path.join(input_path, filename)
        full_output = os.path.join(output_path, filename)
        
        try:
            with open(full_input, 'rb') as f:
                header = f.read(32)
            
            audio = None
            if header.startswith(b'RIFF'):
                audio = AudioSegment.from_wav(full_input)
                print(f"Detected WAV: {filename}")
            elif header.startswith(b'OggS'):
                audio = AudioSegment.from_ogg(full_input)
                print(f"Detected OGG: {filename}")
            elif header.startswith(b'fLaC'):
                audio = AudioSegment.from_file(full_input, "flac")
                print(f"Detected FLAC: {filename}")
            else:
                print(f"Unsupported format: {filename}")
                continue
            
            normalized = normalize(audio)
            change = target_dBFS - normalized.dBFS
            adjusted = normalized.apply_gain(change)
            
            buffer = BytesIO()
            adjusted.export(buffer, format="flac")
            flac_data = buffer.getvalue()
            
            if len(flac_data) < 1024:
                print(f"WARNING: Small file size ({len(flac_data)} bytes) for {filename}")
            
            with open(full_output, 'wb') as f:
                f.write(flac_data)
                
            processed += 1
            print(f"Processed: {filename} ({audio.dBFS:.1f}dB -> {adjusted.dBFS:.1f}dB)")
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
    
    return processed

def main():
    sfx_input = input("\nEnter SFX folder path: ").strip()
    sfx_output = input("Enter output folder for SFX: ").strip()
    music_input = input("\nEnter Music folder path: ").strip()
    music_output = input("Enter output folder for Music: ").strip()
    
    sfx_target = -18.0
    music_target = -23.0
    
    print("\nUsing volume targets:")
    print(f"Sound Effects (SFX): {sfx_target} dBFS")
    print(f"Music: {music_target} dBFS")
    
    print("\nProcessing SFX...")
    sfx_count = process_folder(sfx_input, sfx_output, sfx_target)
    
    print("\nProcessing music...")
    music_count = process_folder(music_input, music_output, music_target)
   
    if sfx_count == 0 and music_count == 0:
        print("\nWARNING: No files processed. Possible issues:")
        print("1. Input folders contain no .data files")
        print("2. Unsupported audio formats")
    elif sfx_count > 0 and music_count > 0:
        print(f"\nSFX: {sfx_count} files processed")
        print(f"Music tracks: {music_count} files processed")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Critical error: {str(e)}")
        sys.exit(1)