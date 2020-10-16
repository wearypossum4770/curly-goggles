import reqeusts
from pathlib import Path
win_checksum ='get-filehash -Algorithm {SHA}}[hash-type] filename'
def add_json_field():
	try:
		import sqlite3
		conn = sqlite3.connect(':memory:')
		cursor = conn.cursor()
		cursor.execute('SELECT JSON(\'{"a": "b"}\')\')
	except:
		print('SQLite3 JSON extentions is not installed\n')
		print('Gathering and installing required files for your OS.\n')
		linux_url = 'https://www.sqlite.org/2020/sqlite-amalgamation-3330000.zip'
		linus_sha3 = 'fb7dfd39009fb40519097b0b1a6af5e8acb17006c848f6d6b7707a4a0c3885c3'
		win_32 = 'https://www.sqlite.org/2020/sqlite-dll-win32-x86-3330000.zip'
		win_64 ='https://www.sqlite.org/2020/sqlite-dll-win64-x64-3330000.zip'
		
		mac_os = 'https://www.sqlite.org/2020/sqlite-tools-osx-x86-3330000.zip'
		file_name = Path(linux_url).name
		response = requests.get(linux_url, stream=True)

		with open (file_name,'wb') as amalgamation:
			for chunk in r.iter_content(chunk_size=1024): 
				if chunk: 
					amalgamation.write(chunk)
	finally:
		sqlLiteDocs = 'https://www.sqlite.org/2020/sqlite-doc-3330000.zip'


		
