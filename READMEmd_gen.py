#!/usr/bin/env python3

import os
import subprocess
import shutil
import sys

def install_ffmpeg():
    print("📹 Installing ffmpeg...")
    try:
        subprocess.run(['sudo', 'apt-get', 'install', 'ffmpeg'], check=True)
    except:
        try:
            subprocess.run(['winget', 'install', 'ffmpeg'], check=True)
        except:
            print("Unsupported operating system. Please install ffmpeg manually.")

def install_script():
    print("📝 Installing script as command...")
    script_name = 'vid_gif_converter'
    script_path = os.path.abspath(__file__)
    try:
        subprocess.run(['sudo', 'cp', script_path, '/usr/local/bin/' + script_name], check=True)
        subprocess.run(['sudo', 'chmod', '+x', '/usr/local/bin/' + script_name], check=True)
        print(f"Installed {script_name} command successfully! 🎉")
    except:
        try:
            subprocess.run(['cp', script_path, '~/.local/bin/' + script_name], check=True)
            subprocess.run(['chmod', '+x', '~/.local/bin/' + script_name], check=True)
            print(f"Installed {script_name} command successfully! 🎉")
        except:
            print("Error installing script as command. Please try manually.")

def convert_videos_to_gifs():
    print("🔄 Converting videos to GIFs...")
    for f in os.listdir():
        if f.lower().endswith(('.mp4', '.webm', '.mkv', '.avi', '.mov', '.wmv', '.flv')):
            try:
                subprocess.run(['ffmpeg', '-i', f, '-vf', 'fps=10', '-r', '10', f'{os.path.splitext(f)[0]}.gif'])
                print(f"Converted {f} to GIF successfully! 🎉")
            except:
                print(f"Error converting {f} to GIF. Skipping...")

if __name__ == "__main__":
    print("👋 Welcome to the video to GIF converter!")
    print("Please follow the instructions below:")
    print("1. This script will install ffmpeg and itself as a command.")
    print("2. It will then convert all videos in the current directory to GIFs.")
    print("3. Please make sure you have the necessary permissions to install software on your system.")
    input("Press Enter to continue...")
    install_ffmpeg()
    install_script()
    convert_videos_to_gifs()
    print("👍 All done! You can now use the 'vid_gif_converter' command to convert videos to GIFs.")
