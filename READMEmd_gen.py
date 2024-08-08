#!/usr/bin/env python3

def generate_readme():
    print("Generating README.md...")
    readme = "# Video to GIF Converter ⚡️\n"
    readme += "A simple script to convert videos to GIFs using ffmpeg. 📹\n\n"
    readme += "## Getting Started 🚀\n"
    readme += "Clone this repository and run the script using `python3 vid_gif_converter.py`.\n"
    readme += "Follow the prompts to install ffmpeg and the script as a command. 💻\n\n"
    readme += "## Usage 📊\n"
    readme += "1. Navigate to the directory containing the videos you want to convert. 🗂️\n"
    readme += "2. Run the `vid_gif_converter` command. 🔄\n"
    readme += "3. The script will convert all videos in the current directory to GIFs. 🎉\n\n"
    readme += "## Requirements 📝\n"
    readme += "* Python 3.x 🐍\n"
    readme += "* Admin privileges to install ffmpeg and the script as a command 🔒\n\n"
    readme += "## Notes 🤔\n"
    readme += "This script assumes you have the necessary permissions to install software on your system. 🚫\n"
    readme += "If you already have ffmpeg installed, you can skip the installation step. 👍\n\n"
    readme += "## License 📜\n"
    readme += "This script is released under the MIT License. 🎉\n\n"
    readme += "## Contributing 🤝\n"
    readme += "Pull requests and issues are welcome! Fork the repository and submit a pull request with your changes. 💻"

    with open("README.md", "w") as f:
        f.write(readme)

    print("README.md generated successfully! 👍")

if __name__ == "__main__":
    generate_readme()
