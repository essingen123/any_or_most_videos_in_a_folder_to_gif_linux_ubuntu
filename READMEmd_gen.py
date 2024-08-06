#!/usr/bin/env python3

import os

def generate_readme():
    print("📄 Generating README.md...")
    readme = "# Video to GIF Converter 📹\n"
    readme += "==========================\n\n"
    readme += "A simple script to convert videos to GIFs using ffmpeg. 🤖\n\n"
    readme += "## Installation 📦\n"
    readme += "---------------\n\n"
    readme += "1. Clone this repository to your local machine.\n"
    readme += "2. Run the script using `python3 vid_gif_converter.py`.\n"
    readme += "3. Follow the prompts to install ffmpeg and the script as a command.\n\n"
    readme += "## Usage 📊\n"
    readme += "-----\n\n"
    readme += "1. Navigate to the directory containing the videos you want to convert.\n"
    readme += "2. Run the `vid_gif_converter` command.\n"
    readme += "3. The script will convert all videos in the current directory to GIFs.\n\n"
    readme += "## Requirements 📝\n"
    readme += "------------\n\n"
    readme += "* Python 3.x\n"
    readme += "* Admin privileges to install ffmpeg and the script as a command\n\n"
    readme += "## Notes 📝\n"
    readme += "-----\n\n"
    readme += "* This script assumes that you have the necessary permissions to install software on your system. If you're running this script on a system where you don't have admin privileges, you may need to modify the script to use a different installation method.\n"
    readme += "* This script uses ffmpeg to convert videos to GIFs. If you already have ffmpeg installed on your system, you can skip the installation step.\n\n"
    readme += "## License 📜\n"
    readme += "-------\n\n"
    readme += "This script is released under the MIT License.\n\n"
    readme += "## Contributing 🤝\n"
    readme += "------------\n\n"
    readme += "Pull requests and issues are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.\n"

    with open("README.md", "w") as f:
        f.write(readme)

    print("👍 README.md generated successfully!")

if __name__ == "__main__":
    generate_readme()
