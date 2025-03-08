def get_books_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	print(get_books_text("books/frankenstein.txt"))

main()

