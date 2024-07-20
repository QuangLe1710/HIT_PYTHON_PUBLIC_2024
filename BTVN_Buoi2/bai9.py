# Bài 9: Cho một số a bất kỳ
# a. Trả về số lượng các bits cần thiết để biểu diễn số a ở dạng nhị phân, không bao gồm phần dấu và các số 0 ở đầu.
# b. Với biến x = “awesome”, sử dụng 3 cách print để cùng đưa ra màn hình “Python is awesome”
# c. Viết chương trình kiểm tra version của python hiện tại


#c) 
import sys
print("Phiên bản Python hiện tại là:", sys.version)

#b)
# cách 1 : Dùng dấu + để nối string 
x = "awesome"
print("Python is " + x)

# cách 2 : dùng f-string 
x = "awesome"
print(f"Python is {x}")

# cách 3 : dùng method format() 
x = "awesome"
print("Python is {}".format(x))


