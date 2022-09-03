"""
File: boggle.py
Name: Zoe
----------------------------------------
This function is to create a Boggle game.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This function is to create a Boggle game. Player need to input 4 rows of
	word list to start the word search.
	"""
	start = time.time()		
	####################
	word_lst = []
	for i in range(1, 5):
		word = input(f'{i} row of letters: ')
		if len(word) != 7:
			print('Illegal input')
			break
		if word[1] != ' ' and word[3] != ' ' and word[5] != ' ':
			print('Illegal input')
			break
		word = word.replace(' ', '')
		word_lst.append(word.lower())

	dict_list = read_dictionary()
	if len(word_lst) == 4:
		ans_lst = []
		find_word(word_lst, dict_list, ans_lst)
		print(f'There are {len(ans_lst)} words in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(word_lst, dict_list, ans_lst):
	"""
	:param word_lst: list, The input word_list by the player.
	:param dict_list: list, An extract dictionary list from the FILE.
	:param ans_lst: list, Contains all the matching words.
	"""
	for x in range(len(word_lst)):
		for y in range(len(word_lst)):
			used_trace_lst = [(x, y)]
			current_word = word_lst[x][y]
			find_word_helper(word_lst, current_word, ans_lst, used_trace_lst, x, y, dict_list)


def find_word_helper(word_lst, current_word, ans_lst, used_trace_lst, x, y, dict_list):
	"""
	:param word_lst: list, The input word_list by the player.
	:param current_word: str, The searched word-combination.
	:param ans_lst: list, Contains all the matching words.
	:param used_trace_lst: list, Contains the found words' coordinates.
	:param x: int, x coordinate of the found word.
	:param y: int, y coordinate of the found word.
	"""
	if current_word in dict_list and current_word not in ans_lst:
		print(f'Found: {current_word}')
		ans_lst.append(current_word)
	else:
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				if 0 <= x+i <= 3:
					if 0 <= y+j <= 3:
						if (x + i, y + j) not in used_trace_lst:
							current_word += word_lst[x+i][y+j]
							used_trace_lst.append((x+i, y+j))
							if has_prefix(current_word, dict_list):
								find_word_helper(word_lst, current_word, ans_lst, used_trace_lst, x+i, y+j, dict_list)
								if current_word in ans_lst:
									find_word_helper(word_lst, current_word, ans_lst, used_trace_lst, x+i, y+j, dict_list)
							current_word = current_word[:-1]
							used_trace_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:return list: An extract dictionary list from the FILE.
	"""
	all_list = []
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= 4:
				all_list.append(line.strip())
	return all_list



def has_prefix(sub_s, dict_list):
	"""
	:param sub_s: str, A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dict_list: list, An extract dictionary list from the FILE.
	:return: boolean, If there is any words with prefix stored in sub_s
	"""
	for word in dict_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
