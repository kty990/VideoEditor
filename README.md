# Video Editor || IN DEVELOPMENT

This is a simple video editor GUI built using the `PyQt5` library. It allows you to open, save, and edit video files.
The aim of this project is to create a robust-ish video editor that is free and open source (following the MIT license).

![preview_v0 0 1](https://user-images.githubusercontent.com/41134070/233322664-355ed4bf-cd57-468e-acd5-faf1bc7bd3ee.png)

## Dependencies

This program has the following dependencies:

- Python 3
- PyQt5
- pickle

## Usage

To use this program as a standalone executable, run this: `pip install pyinstaller` *(if you haven't already)* and then navigate to a local directory containing this program's code and run this: `pyinstaller --onefile ./src/index.py`

To use this program without creating a standalone executable, simply run `python ./src/index.py` in your terminal, or run the file located in `VideoEditor > src > index.py`

## How it works

This program allows you to easily manipulate and edit video content with precision and accuracy. You can insert clips at specific points in time, cut out unwanted content, and create custom video excerpts with multiple tracks. It also includes a feature to add subtitles to your video. With its user-friendly interface, you'll be able to enhance your video content with ease, making it perfect for both personal and professional use.

## Contributing

If you find a bug or have a feature request, please open an issue on GitHub.

## License

This program is released under the MIT License. See the [LICENSE](https://github.com/kty990/VideoEditor/blob/main/LICENSE) file for more information.
