import string
import os
from .fold_remov import ignored_folders
from . import list_app

familiar_formats = []
for key in list_app.dic.keys():
    familiar_formats.append(key)

allowed_characters = set(string.ascii_letters + string.digits)
normalize_dict = {ord(char): "_" for char in string.printable if char not in allowed_characters}

cyr_rom_symb_dict = {
    # Lower (Ukr only)
    '\u0430': 'a',      # а - a
    '\u0431': 'b',      # б - b
    '\u0432': 'v',      # в - v
    '\u0433': 'h',      # г - h
    '\u0491': 'g',      # ґ - g
    '\u0434': 'd',      # д - d
    '\u0435': 'e',      # е - e
    '\u0436': 'zh',     # ж - zh
    '\u0437': 'z',      # з - z
    '\u0438': 'y',      # и - y
    '\u0456': 'i',      # і - i
    '\u0457': 'i',      # ї - i
    '\u0439': 'y',      # й - y
    '\u043a': 'k',      # к - k
    '\u043b': 'l',      # л - l
    '\u043c': 'm',      # м - m
    '\u043d': 'n',      # н - n
    '\u043e': 'o',      # о - o
    '\u043f': 'p',      # п - p
    '\u0440': 'r',      # р - r
    '\u0441': 's',      # с - s
    '\u0442': 't',      # т - t
    '\u0443': 'u',      # у - u
    '\u0444': 'f',      # ф - f
    '\u0445': 'kh',     # х - kh
    '\u0446': 'ts',     # ц - ts
    '\u0447': 'ch',     # ч - ch
    '\u0448': 'sh',     # ш - sh
    '\u0449': 'shch',   # щ - shch
    '\u044e': 'yu',     # ю - yu
    '\u044f': 'ya',     # я - ya
    # Upper (Ukr only)
    '\u0410': 'A',      # А - A
    '\u0411': 'B',      # Б - B
    '\u0412': 'V',      # В - V
    '\u0413': 'H',      # Г - H
    '\u0490': 'G',      # Ґ - G
    '\u0414': 'D',      # Д - D
    '\u0415': 'E',      # Е - E
    '\u0416': 'ZH',     # Ж - ZH
    '\u0417': 'Z',      # З - Z
    '\u0418': 'Y',      # И - Y
    '\u0406': 'I',      # І - I
    '\u0407': 'Ї',      # Ї - I
    '\u0419': 'Y',      # Й - Y
    '\u041a': 'K',      # К - K
    '\u041b': 'L',      # Л - L
    '\u041c': 'M',      # М - M
    '\u041d': 'N',      # Н - N
    '\u041e': 'O',      # О - O
    '\u041f': 'P',      # П - P
    '\u0420': 'R',      # Р - R
    '\u0421': 'S',      # С - S
    '\u0422': 'T',      # Т - T
    '\u0423': 'U',      # У - U
    '\u0424': 'F',      # Ф - F
    '\u0425': 'KH',     # Х - KH
    '\u0426': 'TS',     # Ц - TS
    '\u0427': 'CH',     # Ч - CH
    '\u0428': 'SH',     # Ш - SH
    '\u0429': 'SHCH',   # Щ - SHCH
    '\u042e': 'YU',     # Ю - YU
    '\u042f': 'YA',     # Я - YA
}

def normalize(path):
    os.chdir(path) #definig working location
    for file in os.listdir(): 
        if os.path.isfile(file) and not file.endswith(tuple(familiar_formats)): #ignoring files with unknown format
             continue
        if file in ignored_folders: #ignorign certain folders, files not impacted, since end with ext
            continue
    #translation using dict normalized_name
        name_spl, ext = os.path.splitext(file)
        normalized_name = name_spl.translate(normalize_dict)
        normalized_fullname = f"{normalized_name}{ext}"
        
        translated_name = ''
        for letter in normalized_fullname:
            new_letter = ''
            if letter in cyr_rom_symb_dict:
                new_letter = cyr_rom_symb_dict[letter]
            else:
                new_letter = letter
            translated_name += new_letter
        os.rename(file, translated_name) #renaming folder/file