# Bài 3: Tính các tổng sau:
# a) S(n) = 1 - 2 + 3 - 4 + 5 + .... + (2*n + 1)
# b) S(n) = 1 + ½ + ⅓ + ¼ +.....+1/n
# c) Biện luận nghiệm của phương trình bậc 2 một ẩn


#a) 
n = int(input('Nhập vào giá trị của n: '))
S = 0

for i in range(1, 2 * n + 2):
    if i % 2 == 0:
        S -= i
    else:
        S += i
        
print(f'S({n}) = {S}')


#b) 
n = int(input('Nhập vào giá trị của n: '))
S = 0.0

for i in range(1, n + 1):
    S += 1 / i

print(f'S({n}) = {S}')

#c) 
import cmath

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b*b - 4*a*c

if delta > 0:
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1.real}, x2 = {x2.real}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Phương trình có một nghiệm kép: x = {x}")
else:
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print(f"Phương trình vô nghiệm thực. Hai nghiệm phức: x1 = {x1}, x2 = {x2}")
