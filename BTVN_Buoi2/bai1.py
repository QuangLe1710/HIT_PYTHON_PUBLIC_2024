#bai 1 
#a ) Viết một chương trình yêu cầu người dùng nhập một số nguyên dương. 
# Tính và in ra tổng các chữ số của số đó.
#  Ví dụ: Đối với số 12345, tổng các chữ số là 1 + 2 + 3 + 4 + 5 = 15.

s = input('Nhap vao gia tri cua 1 so nguyen duong : ')
sum = 0 
for i in s :
    sum += int(i) 
print(sum)


#b ) Tính tổng các ước số của một số nguyên dương:
#Viết một chương trình yêu cầu người dùng nhập một số nguyên dương n.
#Tính và in ra tổng của tất cả các ước số của n.
# Ước số của một số là các số mà chia hết cho số đó mà không dư. 
# Ví dụ: Ước số của 6 là 1, 2, 3, và 6.

number = int(input('Nhap vao gia tri cua 1 so nguyen duong : '))
sumDivisor = 0 
print(f'Cac uoc so cua {number} la : ' , end=' ') 
for val in range( 1 , number + 1 ) :
    if ( number % val == 0 ) :
        print( f'{val}' , end=' ' )  
        sumDivisor += val 
    else : 
        continue 
print() 
print(f'Tong cua cac uoc so cua {number} : {sumDivisor}' )  


#c ) Kiểm tra tam giác:
#Viết chương trình yêu cầu người dùng nhập vào 3 số nguyên dương.
#Kiểm tra xem 3 số đó có tạo thành tam giác hay không?
#Nếu có thì đó là tam giác gì?(Cân, đều, vuông, nhọn, tù)

a = int(input('Nhap vao do dai canh 1 cua tam giac : '))
b = int(input('Nhap vao do dai canh 2 cua tam giac : '))
c = int(input('Nhap vao do dai canh 3 cua tam giac : '))

if ( a + b > c ) and ( a + c > b ) and ( b + c > a )  : 
    print( f' {a} và {b} và {c} la 3 canh cua 1 tam giac !!! ')
    if ( a*a + b*b == c*c ) or ( a*a + c*c == b*b ) or ( b*b + c*a == a*a ) :
        print( f'  {a} và {b} và {c} là 3 cạnh của 1 tam giác vuông vì tính chất bình phương của cạnh huyền = tổng bình phương 2 cạnh còn lại !!! ')
    elif ( a == b ) or ( a == c ) or ( b == c ) :
        print( f' {a} và {b} và {c} là 3 cạnh của 1 tam giác cân vì tính chất 1 tam giác có 2 cạnh bằng nhau thì đó là tam giác cân')
    elif ( a == b ) and ( a == c ) and ( b == c ) : 
        print( f' {a} và {b} và {c} là 3 cạnh của 1 tam giác đều vì tính chất 1 tam giác có 3 cạnh đều bằng nhau thì đó là tam giác đều ')  
    elif ( a*a>b*b+c*c ) or ( b*b>a*a+c*c ) or ( c*c >a*a+b*b ) :
        print( f' {a} và {b} và {c} là 3 cạnh của 1 tam giác tù vì tính chất tam giác tù là tam giác có một góc lớn hơn 90 độ !!! ') 
    else : 
        print(f' {a} và {b} và {c} là 3 cạnh của 1 tam giác nhọn')
else : 
    print( f' {a} va {b} va {c} khong la 3 canh cua 1 tam giac !!! ')