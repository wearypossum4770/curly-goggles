package_dict = {
"afr": "Afrikaans",
"amh": "Amharic", 
"ara": "Arabic", 
"asm": "Assamese", 
"aze": "Azerbaijani", 
"aze_cyrl": "Azerbaijani- Cyrilic", 
"bel": "Belarusian", 
"ben": "Bengali", 
"bod": "Tibetan", 
"bos": "Bosnian", 
"bre": "Breton", 
"bul": "Bulgarian", 
"cat": "Catalan Valencian", 
"ceb": "Cebuano", 
"ces": "Czech", 
"chi_sim": "Chinese simplified", 
"chi_tra": "Chinese traditional", 
"chr": "Cherokee", 
"cym": "Welsh", 
"dan": "Danish", 
"deu": "German", 
"dzo": "Dzongkha", 
"ell": "Greek Modern 1453", 
"eng": "English", 
"enm": "English Middle 1100-500", 
"epo": "Esperanto", 
"equ": "Math equation detection module", 
"est": "Estonian", 
"eus": "Basque", 
"fas": "Persian", 
"fin": "Finnish", 
"fra": "French", 
"frk": "Frankish", 
"frm": "French Middle ca 400 1600", 
"gle": "Irish", 
"glg": "Galician", 
"grc": "Greek Ancient to 453", 
"guj": "Gujarati", 
"hat": ["Haitian","Haitian Creole"], 
"heb": "Hebrew", 
"hin": "Hindi", 
"hrv": "Croatian", 
"hun": "Hungarian", 
"iku": "Inuktitut", 
"ind": "Indonesian", 
"isl": "Icelandic", 
"ita": "Italian", 
"ita_old": "Italian - Old", 
"jav": "Javanese", 
"jpn": "Japanese", 
"kan": "Kannada", 
"kat": "Georgian", 
"kat_old": "Georgian - Old", 
"kaz": "Kazakh", 
"khm": "Central Khmer", 
"kir": ["Kirghiz","Kyrgyz"], 
"kmr": "Kurdish Kurmanji", 
"kor": "Korean", 
"kor_vert": "Korean vertical", 
"kur": "Kurdish", 
"lao": "Lao", 
"lat": "Latin", 
"lav": "Latvian", 
"lit": "Lithuanian", 
"ltz": "Luxembourgish", 
"mal": "Malayalam", 
"mar": "Marathi", 
"mkd": "Macedonian", 
"mlt": "Maltese", 
"mon": "Mongolian", 
"mri": "Maori", 
"msa": "Malay", 
"mya": "Burmese", 
"nep": "Nepali", 
"nld": "Dutch Flemish", 
"nor": "Norwegian", 
"oci": "Occitan post 1500", 
"ori": "Oriya", 
"osd": "Orientation and script detection module", 
"pan": ["Panjabi", "Punjabi"], 
"pol": "Polish", 
"por": "Portuguese", 
"pus": "Pushto Pashto", 
"que": "Quechua", 
"ron": ["Romanian Moldavian", "Moldovan"], 
"rus": "Russian", 
"san": "Sanskrit", 
"sin": "Sinhala Sinhalese", 
"slk": "Slovak", 
"slv": "Slovenian", 
"snd": "Sindhi", 
"spa": "Spanish Castilian", 
"spa_old": "Spanish Castilian - Old", 
"sqi": "Albanian", 
"srp": "Serbian", 
"srp_latn": "Serbian- Latin", 
"sun": "Sundanese", 
"swa": "Swahili", 
"swe": "Swedish", 
"syr": "Syriac", 
"tam": "Tamil", 
"tat": "Tatar", 
"tel": "Telugu", 
"tgk": "Tajik", 
"tgl": "Tagalog", 
"tha": "Thai", 
"tir": "Tigrinya", 
"ton": "Tonga", 
"tur": "Turkish", 
"uig": "Uighur Uyghur",
"ukr":"Ukrainian",
"urd":"Urdu)", 
"uzb":"Uzbek)", 
"uzb_cyrl":"Uzbek - Cyrilic)",
"vie":"Vietnamese)",
"yid":"Yiddish",
"yor":"Yoruba",

}


"sudo apt install tesseract-ocr tesseract-ocr-{LANGUAGE_CODE}"
cmd_cli={}
# ~ cmd_cli = {
# ~ DPI_OPTION:"--dpi"

# ~ }

TESSERACT_LANGUAGE = "-l"
LANGUAGE_CODE=""
"tesseract {IMAGE_TO_READ} {FILENAME_NO_EXT} {cmd_cli.get('TESSERACT_LANGUAGE')} {cmd_cli.get('LANGUAGE_CODE')}{cmd_cli.get('DPI_OPTION')} cmd_cli.get("DPI_VALUE")}"
"https://www.howtogeek.com/682389/how-to-do-ocr-from-the-linux-command-line-using-tesseract/amp/#"
