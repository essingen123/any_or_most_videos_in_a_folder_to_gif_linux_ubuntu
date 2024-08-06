#!/usr/bin/env python3
#file: vid2gif_converter.py

import os
import subprocess
import shutil
import sys
import platform
import argparse
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def install_ffmpeg():
    """Install ffmpeg on the system"""
    logging.info("Installing ffmpeg...")
    if platform.system() == "Linux":
        package_managers = [
            ['sudo', 'apt-get', 'install', 'ffmpeg'],
            ['sudo', 'yum', 'install', 'ffmpeg'],
            ['sudo', 'pacman', '-S', 'ffmpeg'],
            ['sudo', 'zypper', 'install', 'ffmpeg']
        ]
        for package_manager in package_managers:
            try:
                subprocess.run(package_manager, check=True)
                return
            except:
                pass
        logging.error("Unsupported Linux distribution. Please install ffmpeg manually.")
    elif platform.system() == "Windows":
        package_managers = [
            ['winget', 'install', 'ffmpeg'],
            ['choco', 'install', 'ffmpeg'],
            ['scoop', 'install', 'ffmpeg']
        ]
        for package_manager in package_managers:
            try:
                subprocess.run(package_manager, check=True)
                return
            except:
                pass
        logging.error("Unsupported Windows package manager. Please install ffmpeg manually.")
    elif platform.system() == "Darwin":  # macOS
        package_managers = [
            ['brew', 'install', 'ffmpeg'],
            ['port', 'install', 'ffmpeg']
        ]
        for package_manager in package_managers:
            try:
                subprocess.run(package_manager, check=True)
                return
            except:
                pass
        logging.error("Unsupported macOS package manager. Please install ffmpeg manually.")

def install_script():
    """Install the script as a command"""
    logging.info("Installing script as command...")
    script_name = 'vid_gif_converter'
    script_path = Path(__file__).resolve()
    if platform.system() == "Linux" or platform.system() == "Darwin":
        try:
            subprocess.run(['sudo', 'cp', str(script_path), '/usr/local/bin/' + script_name], check=True)
            subprocess.run(['sudo', 'chmod', '+x', '/usr/local/bin/' + script_name], check=True)
            logging.info(f"Installed {script_name} command successfully!")
        except:
            try:
                subprocess.run(['cp', str(script_path), '~/.local/bin/' + script_name], check=True)
                subprocess.run(['chmod', '+x', '~/.local/bin/' + script_name], check=True)
                logging.info(f"Installed {script_name} command successfully!")
            except:
                logging.error("Error installing script as command. Please try manually.")
    elif platform.system() == "Windows":
        try:
            subprocess.run(['copy', str(script_path), 'C:\\Windows\\System32\\' + script_name + '.py'], check=True)
            logging.info(f"Installed {script_name} command successfully!")
        except:
            logging.error("Error installing script as command. Please try manually.")

def convert_videos_to_gifs(output_dir):
    print("🔄 Converting videos to GIFs...")
    for f in os.listdir():
        if f.lower().endswith(('.mp4', '.webm', '.mkv', '.avi', '.mov', '.wmv', '.flv')):
            try:
                output_file = os.path.join(output_dir, os.path.splitext(f)[0] + '.gif')
                subprocess.run(['ffmpeg', '-i', f, '-vf', 'fps=10', '-r', '10', output_file])
                print(f"Converted {f} to GIF successfully! 🎉")
            except:
                print(f"Error converting {f} to GIF. Skipping...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Video to GIF converter')
    parser.add_argument('--output', help='Output directory for converted GIFs')
    parser.add_argument('--dry-run', action='store_true', help='Dry run mode')
    args = parser.parse_args()

    print("👋 Welcome to the video to GIF converter!")
    print("Please follow the instructions below:")
    print("1. This script will install ffmpeg and itself as a command.")
    print("2. It will then convert all videos in the current directory to GIFs.")
    print("3. Please make sure you have the necessary permissions to install software on your system.")
    input("Press Enter to continue...")

    install_ffmpeg()
    install_script()

    if args.output:
        output_dir = args.output
    else:
        output_dir = os.getcwd()

    if args.dry_run:
        print("Dry run mode enabled. No files will be converted.")
    else:
        convert_videos_to_gifs(output_dir)

    print("👍 All done")
