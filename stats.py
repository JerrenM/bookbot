def get_num_words(text):
        count = 0
        for word in text.split():
                count+=1
        return count

def count_chars(text):
	char_counts = {}
	for char in text:
		char = char.lower()
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts
