import sys
def get_book_text(filepath):
        with open(filepath) as f:
                file_contents = f.read()
        return file_contents

def word_count(filename):
        split_book = (filename)
        split_book = get_book_text(filename).split()
        num_words = 0
        for i in split_book:
                num_words += 1
        print(f"Found {num_words} total words")

def char_count(filename):
	char_count =  filename
	char_dict = {}
	char_count = get_book_text(filename).lower()
	for i in char_count:
		if i in char_dict:
			char_dict[i] += 1
		else:
			char_dict[i] = 1
	return char_dict

def sort_on(dict):
        return dict["num"]

def char_sort(filename):
	char_sort = [ {"char": key, "count": value} for key, value in char_count(filename).items()]
	char_sort.sort(key=lambda x: x["count"], reverse=True)
	return char_sort

