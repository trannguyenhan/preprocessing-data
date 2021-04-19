import os
from standardize import tien_xu_li

# 27 nhãn
list_name_categories = os.listdir("raw-data/10-topics/Test_Full")

def get_list_content(path):
	list_content_file = []
	list_name_file = os.listdir(path)
	for name_file in list_name_file : 
		# tạo đường dẫn của file từ thư muc cha và tên file 
		path_file = path + "/" + name_file
		# đọc file 
		file = open(path_file, "r", encoding="utf-16")
		# lấy nội dung của file 
		content_file = file.read()
		# chuẩn hóa nội dung file 
		content_file = tien_xu_li(content_file)
		# ghi file vào list 
		list_content_file.append(content_file)

	return list_content_file

def write_file_output(list_content_file, category, isTrain):
	path_file = ""
	if isTrain : 
		path_file = "clean-data/train/" + category + ".txt"
	else : 
		path_file = "clean-data/test/" + category + ".txt"

	file_output = open(path_file, "w", encoding="utf-8")
	for content_file in list_content_file : 
		file_output.write(content_file + "\n")

	print("write done " + category + " in path " + path_file + "!")
	file_output.close()

# chuẩn hóa tất cả các file của tất cả các nhãn 
def standardize_all_categories(train_or_test):
	for name_categories in list_name_categories : 
		path_file_output = "raw-data/" + train_or_test + "/" + name_categories
		list_content_file = get_list_content(path_file_output)	

		if train_or_test == "10-topics/Train_Full":
			write_file_output(list_content_file, name_categories, True)
		else :
			write_file_output(list_content_file, name_categories, False)

if __name__ == "__main__":
	# main
	standardize_all_categories("10-topics/Test_Full")
	standardize_all_categories("10-topics/Train_Full")
