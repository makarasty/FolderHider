
from win32file import GetFileAttributes
from keyboard import add_hotkey, wait
from os import system, getlogin
from ctypes import windll

FolderPath = open('data.cfg', 'r').readlines()[1]

L_BLUE = '\033[94m'
GREEN = '\033[32m'
WHITE = '\033[0m'
GREY = '\033[90m'
PINK = '\033[95m'
BLUE = '\033[34m'
BOLD = '\033[1m'
RED = '\033[31m'

if __name__ == '__main__':
	def main():
		while 1:
			system('@cls')
			print(f'{L_BLUE}| {WHITE}Привіт {RED}{getlogin()}{WHITE}, Введи потрібний тобі {L_BLUE}пункт{WHITE}!\n')
			print(f'{L_BLUE}| {WHITE}Зараз папка - {TestFolderAttributes(FolderPath)}')
			print(f'{L_BLUE}| {WHITE}1 {L_BLUE}- {WHITE}Показати папку')
			print(f'{L_BLUE}| {WHITE}2 {L_BLUE}- {WHITE}Сховати папку')
			print(f'{L_BLUE}| {WHITE}3 {L_BLUE}- {WHITE}Відкрити папку')
			try:
				Input = int(input(f'\n{L_BLUE}| {WHITE}Ти вводиш: {L_BLUE}'))
			except:
				main()
			if Input == 1:
				system('@cls')
				windll.kernel32.SetFileAttributesW(FolderPath, 128)
				print(
					f'\n{L_BLUE}| {WHITE}Папка {GREEN}показана{WHITE}! {GREY}(ENTER в меню)\n')
				input('')
			elif Input == 2:
				system('@cls')
				windll.kernel32.SetFileAttributesW(FolderPath, 2)
				print(
					f'\n{L_BLUE}| {WHITE}Папка {PINK}схована{WHITE}! {GREY}(ENTER в меню)\n')
				input('')
			elif Input == 3:
				system('@cls')
				system(f'@start "" "{FolderPath}"')
				print(
					f'\n{L_BLUE}| {WHITE}Папка {L_BLUE}відкрита{WHITE}! {GREY}(ENTER в меню)\n')
				input('')

	def TestFolderAttributes(folder):
		Attridutes = GetFileAttributes(folder)
		if Attridutes == 18:
			return f'{PINK}СХОВАНА'
		if Attridutes == 16:
			return f'{GREEN}ПОКАЗАНА'
		else:
			f'{RED}НЕВІДОМО'
	add_hotkey('esc + /', main)
	wait('space')
