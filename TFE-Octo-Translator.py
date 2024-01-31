from googletrans import Translator
import time

translator = Translator()
counter = 0
with open('subtitles-en.txt', encoding='cp437') as file:
    for line in file:
        counter += 1
        if '"' in line and counter > 0:  # use the line number to start from a desired line, also see below
            start = line.find('"')
            end = line.rfind('"')
            original_part = line[start + 1:end]
            # 'it' is the code for italian, use the code you want
            translated_part = translator.translate(text=original_part, src='en', dest='it', )
            time.sleep(0.2)  # a pause to avoid too many calls for second to google servers
            new_line = line[:start + 1] + translated_part.text + line[end::]
            # change the name of the subtitle file, also below. Change the encoding if needed by your language
            with open('subtitles-it.txt', 'a', encoding="utf8") as new_file:
                new_file.write(new_line)
                print(line)
                print(new_line)
        elif '"' not in line and counter > 0:  # again use the line number to start from the same desired line
            # change the name of the subtitle file again or the encoding
            with open('subtitles-it.txt', 'a', encoding="utf8") as new_file:
                new_file.write(line)
                print(line)
input('THE END. Press a key to exit.')
