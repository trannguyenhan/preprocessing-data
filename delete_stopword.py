import os
from dictionary import get_dictionary

stopword = []
lower_word = []

def remove_stopword(dictionary):
	new_dictionary = {}
	f_stopword = open("stopword.txt", "r", encoding="utf-8")
	data_stopword = f_stopword.read().split("\n")

	for data in data_stopword : 
		stopword.append(data)

	for word in dictionary : 
		if word not in stopword :
			new_dictionary[word] = dictionary.get(word)

	print("size of dictionary after remove stop word : " + str(len(new_dictionary)))
	return new_dictionary

def remove_lower_word(dictionary):
	new_dictionary = {}
	for word in dictionary : 
		if dictionary[word] < 30: 
			lower_word.append(word)
		else :
			new_dictionary[word] = dictionary.get(word)

	print("size of dictionary after remove lower word : " + str(len(new_dictionary)))
	return new_dictionary


# def remove_stopword_and_lowerword(dictionary):
	# list_name = os.listdir("clean-data/train/")
	# for name_file in list_name : 
	# 	# xử lý tập train trước 
	# 	data_f_train = open("clean-data/train/" + name_file, "r", encoding="utf-8").read()
	# 	data_train = open("data/train/" + name_file, "w", encoding="utf-8")
	# 	list_data_f_train = data_f_train.split("\n")

	# 	# xử lý từng văn bản trong mỗi nhãn 
	# 	for i_data_f_train in list_data_f_train : 
	# 		text = ""
	# 		list_i_data_f_train = i_data_f_train.split(" ")
	# 		for word in list_i_data_f_train : 
	# 			if word not in stopword and word not in lower_word : 
	# 				text += word + " "
	# 		data_train.write(text + "\n")
	# 	print("done! " + name_file)

def print_dictionary(dictionary):
	f = open("dictionary.txt", "w", encoding="utf-8")
	for word in dictionary :
		f.write(word + " " + str(dictionary.get(word)) + "\n")

if __name__ == "__main__":
	dictionary = {}
	dictionary = get_dictionary("clean-data")
	print("size of dictionary before remove stop word and lower word : " + str(len(dictionary)))

	dictionary = remove_stopword(dictionary)
	dictionary = remove_lower_word(dictionary)

	print_dictionary(dictionary)


	