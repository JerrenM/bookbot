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

def sort_dict(dictionary):
	report = []
	for key, value in dictionary.items():
		if key.isalpha():
			char_info = {"key": key, "value": value}
			report.append(char_info)
	report.sort(reverse=True, key=lambda char_info:char_info["value"])
	
	
	
	return report