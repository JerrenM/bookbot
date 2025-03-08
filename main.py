from stats import get_num_words, count_chars, sort_dict
# import os
# print("Current working directory:", os.getcwd())
def get_books_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	filepath = "bookbot/books/frankenstein.txt"
	text = get_books_text(filepath)
	word_count = get_num_words(text)
	dict = count_chars(text)
	report = sort_dict(dict)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")

	for item in report:
		char = item["key"]
		count = item["value"]
		print(f"{char}: {count}")
	
	print("============= END ===============")

main()
