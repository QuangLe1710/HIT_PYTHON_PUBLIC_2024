# Bài 2:  Cho 2 số a, b bất kỳ. Hãy in ra màn hình:
# a.    a cộng b
# b.    a trừ b
# c.    a nhân b
# d.    a chia lấy nguyên b
# e.    a mũ b
# f.     a chia dư b
# g.    so sánh a và b (lớn hơn, nhỏ hơn hay bằng)
# h.    a AND b
# i.     a OR b
# j.     a XOR b
# k.   NOT a == b
# l.    a dịch phải 1 đơn vị
# m.  a dịch trái 1 đơn vị

import random

a = int( random.random()*100 ) 
print( f'Gia tri cua a : {a}' ) 

b = int( random.random()*100 ) 
print( f'Gia tri cua a : {b}' ) 

# Thực hiện các phép toán và in kết quả
print(f'a + b = {a + b}')           # a cộng b
print(f'a - b = {a - b}')           # a trừ b
print(f'a * b = {a * b}')           # a nhân b
print(f'a // b = {a // b}')         # a chia lấy nguyên b
print(f'a ** b = {a ** b}')         # a mũ b
print(f'a % b = {a % b}')           # a chia dư b

# So sánh a và b
if a > b:
    print(f'a ({a}) lớn hơn b ({b})')
elif a < b:
    print(f'a ({a}) nhỏ hơn b ({b})')
else:
    print(f'a ({a}) bằng b ({b})')

# Các phép toán bitwise và logic
print(f'a AND b = {a & b}')         # a AND b
print(f'a OR b = {a | b}')          # a OR b
print(f'a XOR b = {a ^ b}')         # a XOR b
print(f'NOT a == b = {not a == b}') # NOT a == b
print(f'a dịch phải 1 đơn vị = {a >> 1}') # a dịch phải 1 đơn vị
print(f'a dịch trái 1 đơn vị = {a << 1}') # a dịch trái 1 đơn vị



