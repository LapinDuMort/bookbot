import sys
def main():
	print(get_book_text(sys.argv))

from stats import word_count, char_count, char_sort

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

filename = sys.argv[1]
print("============ BOOKBOT ============")
print(f"Analyzing book found at {filename}...")
print("----------- Word Count ----------")
word_count(filename)
print("--------- Character Count -------")
char_sort = char_sort(filename)
for item in char_sort:
	if item["char"].isalpha():
		print(f"{item["char"]}: {item["count"]}")
print("============= END ===============")
