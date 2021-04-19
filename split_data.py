# Module dùng để chia lại số lượng tập train và test
# Đồng thời gộp lại tập train và test để thành tập Full nếu cân 

import os

def data_aggregation():
	list_name = os.listdir("clean-data/train/")

	for name_file in list_name : 
		f_train = open("clean-data/train/" + name_file, "r", encoding="utf-8")
		f_test = open("clean-data/test/" + name_file, "r", encoding="utf-8")

		f_all = open("clean-data/full/" + name_file, "w", encoding="utf-8")

		data_f_train = f_train.read()
		data_f_test = f_test.read()

		f_all.write(data_f_train + "\n" + data_f_test)
		print("write done " + name_file)


def split_data(percent):
	list_name = os.listdir("clean-data/train/")

	for name_file in list_name : 
		f_all = open("clean-data/full/" + name_file, "r", encoding="utf-8")
		data_f_all = f_all.read()

		list_data_f_all = data_f_all.split("\n")
		size_data_f_all = len(list_data_f_all)

		size_data_f_train = int(size_data_f_all * 70 / 100) # lấy số lương văn bản cho tập train 
		f_train = open("clean-data/train/" + name_file, "w", encoding="utf-8")
		f_test = open("clean-data/test/" + name_file, "w", encoding="utf-8")

		cnt = 0
		for i_data_f_all in list_data_f_all : 
			if cnt < size_data_f_train : # nếu cnt < dung lượng tập train thì ghi vào tập train, không thì ghi vào tập test 
				if i_data_f_all != "" : 
					f_train.write(i_data_f_all + "\n")	
			else : # ghi ra tập test 
				if i_data_f_all != "" :
					f_test.write(i_data_f_all + "\n")

			cnt += 1

		print("[FULL] " + name_file + " : " + str(len(open("clean-data/full/"  + name_file, "r", encoding="utf-8").read().split("\n"))))
		print("[TRAIN] " + name_file + " : " + str(len(open("clean-data/train/" + name_file, "r", encoding="utf-8").read().split("\n"))))
		print("[TEST] " + name_file + " : " + str(len(open("clean-data/test/" + name_file, "r", encoding="utf-8").read().split("\n"))))

if __name__ == "__main__":
	# Nếu cần gộp data thì hãy bỏ comment để sử dụng hàm này 
	# data_aggregation()
	split_data(70)