from stats import get_num_words, count_chars

def get_books_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	filepath = "books/frankenstein.txt"
	text = get_books_text(filepath)
	word_count = get_num_words(text)
	print(f"{word_count} words found in the document")
	dict = count_chars(text)
	print(dict)
main()
