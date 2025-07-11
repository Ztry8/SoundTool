import os
from pydub import AudioSegment
from pydub.effects import normalize

def process_folder(input_path, output_path, target_dBFS):
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
            
            if header.startswith(b'RIFF'):
                audio = AudioSegment.from_wav(full_input)
            elif header.startswith(b'OggS'):
                audio = AudioSegment.from_ogg(full_input)
            else:
                print(f"Unsupported format: {filename}")
                continue
            
            normalized = normalize(audio)
            change = target_dBFS - normalized.dBFS
            adjusted = normalized.apply_gain(change)
            
            wav_data = adjusted.export(format='wav').read()
            with open(full_output, 'wb') as f:
                f.write(wav_data)
                
            processed += 1
            print(f"Processed: {filename} ({audio.dBFS:.1f}dB -> {adjusted.dBFS:.1f}dB)")
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
    
    return processed

def main():
    print("=" * 50)
    print("AUDIO NORMALIZATION TOOL")
    print("=" * 50)
    
    sfx_input = input("\nEnter SFX folder path: ").strip()
    sfx_output = input("Enter output folder for SFX: ").strip()
    music_input = input("\nEnter Music folder path: ").strip()
    music_output = input("Enter output folder for Music: ").strip()
    
    sfx_target = -18.0
    music_target = -23.0
    
    print("\nUsing volume targets:")
    print(f"Sound Effects (SFX): {sfx_target} dBFS")
    print(f"Music: {music_target} dBFS")
    
    print("\n" + "=" * 30)
    print("PROCESSING SOUND EFFECTS")
    print("=" * 30)
    sfx_count = process_folder(sfx_input, sfx_output, sfx_target)
    
    print("\n" + "=" * 30)
    print("PROCESSING MUSIC")
    print("=" * 30)
    music_count = process_folder(music_input, music_output, music_target)
    
    print("\n" + "=" * 50)
    print("PROCESSING COMPLETE!")
    print(f"Sound Effects: {sfx_count} files")
    print(f"Music tracks: {music_count} files")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
    except Exception as e:
        print(f"Critical error: {str(e)}")