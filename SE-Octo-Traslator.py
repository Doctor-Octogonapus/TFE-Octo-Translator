from googletrans import Translator
import sys

print('This script will translate Scorched Earth')
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

translator = Translator()

if len(sys.argv) == 1:
    line_start = 0
else:
    if sys.argv[1].isdecimal():
        line_start = abs(int(sys.argv[1]))
    else:
        line_start = 0

subtitles = input('Insert the filename you want to translate: ')
counter = 0

with open(subtitles) as file:
    for line in file:
        counter += 1
        if counter >= line_start:
            translated_line = translator.translate(text=line.strip('\n'), src='en', dest=destination_language)
            with open(destination_language.upper() + subtitles, 'a') as new_file:
                new_file.write(translated_line.text + '\n')
                print(line)
                print(translated_line.text)
                print('-' * 20)
input('THE END. Press a key to exit.')
