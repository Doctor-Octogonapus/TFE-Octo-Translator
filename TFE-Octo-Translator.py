from googletrans import Translator
import time
import sys

print('This script will translate Star Wars: Dark Forces')
print('to your language using the googletrans package.')
print('')

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'ar': 'arabic',
    'be': 'belarusian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'zh-CN': 'chinese_simplified',
    'zh-TW': 'chinese_traditional',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'gl': 'galician',
    'de': 'german',
    'el': 'greek',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hu': 'hungarian',
    'is': 'icelandic',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'ko': 'korean',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'mk': 'macedonian',
    'ms': 'malay',
    'mt': 'maltese',
    'no': 'norwegian',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'sk': 'slovak',
    'sl': 'slovenian',
    'es': 'spanish',
    'sw': 'swahili',
    'sv': 'swedish',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'yi': 'yiddish',
}


def show_languages():
    print('Do you want to see the codes for the')
    answer = input('supported languages? (y/n) Default: No > ')
    if answer in ['y', 'Y']:
        print("""
af: afrikaans               sq: albanian                ar: arabic                  
be: belarusian              bg: bulgarian               ca: catalan                 
zh-CN: chinese_simplified   zh-TW: chinese_traditional  hr: croatian                
cs: czech                   da: danish                  nl: dutch                   
en: english                 eo: esperanto               et: estonian
tl: filipino                fi: finnish                 fr: french
gl: galician                de: german                  el: greek
iw: hebrew                  hi: hindi                   hu: hungarian
is: icelandic               id: indonesian              ga: irish
it: italian                 ja: japanese                ko: korean
la: latin                   lv: latvian                 lt: lithuanian
mk: macedonian              ms: malay                   mt: maltese
no: norwegian               fa: persian                 pl: polish
pt: portuguese              ro: romanian                ru: russian
sr: serbian                 sk: slovak                  sl: slovenian
es: spanish                 sw: swahili                 sv: swedish
th: thai                    tr: turkish                 uk: ukrainian
vi: vietnamese              cy: welsh                   yi: yiddish
""")


show_languages()

destination_language = ''


def ask_dest_lang():
    global destination_language
    destination_language = input('Insert the code of your language: ')
    if destination_language not in LANGUAGES:
        print('Insert a correct value')
        ask_dest_lang()


ask_dest_lang()

# print(destination_language)
translator = Translator()

if len(sys.argv) == 1:
    line_start = 0
else:
    if sys.argv[1].isdecimal():
        line_start = abs(int(sys.argv[1]))
    else:
        line_start = 0

counter = 0
with open('subtitles-en.txt', encoding='cp437') as file:
    for line in file:
        counter += 1
        if '"' in line and counter >= line_start:  # use the line number to start from a desired line, also see below
            start = line.find('"')
            end = line.rfind('"')
            original_part = line[start + 1:end]
            # 'it' is the code for italian, use the code you want
            translated_part = translator.translate(text=original_part, src='en', dest=destination_language, )
            time.sleep(0.2)  # a pause to avoid too many calls for second to google servers
            new_line = line[:start + 1] + translated_part.text + line[end::]
            # change the name of the subtitle file, also below. Change the encoding if needed by your language
            with open('subtitles-' + destination_language + '.txt', 'a', encoding="utf8") as new_file:
                new_file.write(new_line)
                print(line)
                print(new_line)
        elif '"' not in line and counter >= line_start:  # again use the line number to start from the same desired line
            # change the name of the subtitle file again or the encoding
            with open('subtitles-' + destination_language + '.txt', 'a', encoding="utf8") as new_file:
                new_file.write(line)
                print(line)
input('THE END. Press a key to exit.')
