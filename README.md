# Video Editor

This is a simple video editor GUI built using Python's `tkinter` library. It allows you to open, save, and edit video files.

## Dependencies

This program has the following dependencies:

- Python 3
- tkinter
- pickle

## Usage

To use this program as a standalone executable, run this: `pip install pyinstaller` *(if you haven't already)* and then navigate to a local directory containing this program's code and run this: `pyinstaller --onefile ./src/index.py`

To use this program without creating a standalone executable, simply run `src/index.py`

## How it works

This program uses tkinter to create a GUI with a menu bar and several frames. The frames are arranged in a grid pattern, with three frames on the top level and three frames on the bottom level. The top level frames are evenly spaced, while the bottom level frames take up the remaining space.

When the user resizes the window, the program automatically resizes the frames to fit the new window size. The labels on the frames are also resized to fit the new frame sizes.

## Contributing

If you find a bug or have a feature request, please open an issue on GitHub.

## License

This program is released under the MIT License. See the [LICENSE](https://github.com/kty990/VideoEditor/blob/main/LICENSE) file for more information.
