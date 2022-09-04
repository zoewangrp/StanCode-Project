"""
File: anagram.py
Name: Zoe
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This function recursively finds all the anagrams for the word.
    """
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input(f'Find anagrams for: ')
        if word == EXIT:
            break

        start = time.time()
        dict_lst = []
        read_dictionary(len(word), dict_lst)
        ans_lst = []
        find_anagrams(word, ans_lst, dict_lst)
        print(f'{len(ans_lst)} anagrams: {ans_lst}')

        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(word_length, dict_lst):
    global FILE
    with open(FILE, 'r') as f:
        for line in f:
            if len(line.strip()) == word_length:
                dict_str = line.strip()
                dict_lst.append(dict_str)


def find_anagrams(word, ans_lst, dict_lst):
    print(f'Searching...')
    find_anagrams_helper(word, ans_lst, '', [], dict_lst)


def find_anagrams_helper(word, ans_lst, current_str, used_index_lst, dict_lst):
    # Base case
    if len(current_str) == len(word):
        if current_str in dict_lst and current_str not in ans_lst:
            print(current_str)
            print('Searching...')
            ans_lst.append(current_str)

    # Recursive case
    else:
        for i in range(len(word)): 
            if i not in used_index_lst:  
                # Choose
                current_str += word[i]
                used_index_lst.append(i)

                # Explore
                if has_prefix(current_str, dict_lst): 
                    find_anagrams_helper(word, ans_lst, current_str, used_index_lst, dict_lst)

                # Un choose 
                current_str = current_str[:-1] 
                used_index_lst.pop() 


def has_prefix(sub_s, dict_lst):
    for word in dict_lst:
        word.startswith(sub_s)
        return True
    return False


if __name__ == '__main__':
    main()
