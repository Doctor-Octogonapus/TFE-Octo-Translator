<h1 style="text-align: center;">TFE-Octo-Translator</h1>

A simple Python script to translate **The Force Engine** using the Python Googletrans package.

### Prerequisites:
 - Python 3.8+
 - Packages: googletrans, httpcore, httpx

### Instructions:
Install googletrans, httpcore, httpx with:

    pip install -U googletrans, httpcore httpx

Launch it in the directory with the file subtitles-en.txt to translate
the entire file. If you specify a number after TFE-Octo-Translator.py,
the translation will start from that line number, skipping the rest.

Example:

    python TFE-Octo-Translator.py 200

It will start the translation from the line 200.
A file will be created in the same folder with the name
subtitles-xx.txt, where xx will be your 2-letters language code.
If you start multiple time the script it will append the text to the pre-existing file.
If you don't want that, just delete, move or rename the old file.

### Remember: 
The Force Engine ships with a free font containing latin characters.
If you want to translate the file in a language not supported by that charset, just go to [Google Fonts](https://fonts.google.com/) and download a free font. I suggest a font from the Noto style.
For example for Japanese just download [Noto Sans Japanese - Google Fonts](https://fonts.google.com/noto/specimen/Noto+Sans+JP?subset=japanese&noto.script=Hira), open the zip and then copy the file NotoSansJP-Regular.ttf in the TheForceEngine\Fonts\ folder.








