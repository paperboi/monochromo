# Wind Down Routine for Windows

A simple Python script to automatically render the system color display to greyscale from 10PM to 7 AM. Meant for devices running on Windows OS. Inspired by the Grayscale feature of Google's [Digital Wellbeing](https://wellbeing.google/) app (or special settings) for Android devices.

## Pre-requisites

You need Python 3 installed on your machine.

## Setup

Clone this repository (or download it as a zip and extract it to a directory).
Within this directory, execute

```bash
pip install -r requirements.txt
```

## Usage

To test out the script, open your command line interface and run

```bash
pythonw winddown.pyw
```

To run it as a background process at startup,

1. Create a batch file with the following format:
   ```
   "C:\Python38\pythonw.exe" "C:\Users\path\to\winddown.pyw"
   ```   
2. Create a shortcut to the batch file.
3. Once the shortcut is created, right-click the shortcut file and select Cut.
4. Open the Run command window using <kbd>Ctrl</kbd>+<kbd>R</kbd>, and type ```shell:startup``` to open the Startup folder.
5. Once the Startup folder is opened, click the Home tab at the top of the folder and select Paste to paste the shortcut file into the Startup folder.
