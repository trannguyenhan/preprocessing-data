import os
import re

list_name_file = os.listdir("clean-data/train/")

# truy cập vào tập train và tạo từ điển cho tập train 
def get_dictionary(folder):
	dictionary = {}
	for name_file in list_name_file : 
		path_file = folder + "/train/" + name_file
		file = open(path_file, "r", encoding="utf-8")
		data = file.read()

		list_words = re.split('[ \n]', data)
		for word in list_words : 
			if word not in dictionary : 
				dictionary[word] = 0
			else : 
				dictionary[word] += 1
		print("done! " + name_file)

	return dictionary
		
# lấy ra dung lượng của từ điển 
def size_of_dictionary(dictionary):
	cnt = 0
	for word in dictionary : 
		cnt += 1

	print("size of dictionary : " + str(cnt))

if __name__ == "__main__":
	# lấy từ điển 
	dictionary = get_dictionary("clean-data")

	# in số lượng từ điển 
	size_of_dictionary(dictionary)
