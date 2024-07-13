Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?
        -   Python là ngôn ngữ thông dịch điển hình . Vì vậy việc chạy các chương trình Python cần sự hỗ trợ của trình thông dịch. Chỉ cần bạn cài đặt các trình thông dịch khác nhau trên các nền tảng khác nhau, mã của bạn có thể chạy bất cứ lúc nào mà không cần lo lắng về bất kỳ vấn đề tương thích nào. Viết, chạy ở mọi nơi ".
        -   Python hỗ trợ hầu hết các nền tảng phổ biến, chẳng hạn như Linux, Windows, Mac OS ... , mã Python bạn viết có thể chạy chính xác trên các nền tảng này mà không cần sửa đổi. Từ đó ta thấy được khả năng hay tính di động và linh hoạt của Python cực mạnh 


Bài 2 ( Tìm hiểu trước ) 

        -   Đối với Python, ngôn ngữ lập trình có CÁC KIỂU DỮ LIỆU sau được tích hợp sẵn theo mặc định, cụ thể như :
            +   Text Type: str
            +    Numeric Types:  int, float, complex
            +   Sequence Types: list, tuple, range
            +   Mapping Type: dict
            +   Set Types: set, frozenset
            +   Boolean Type: bool
            +   Binary Types: bytes, bytearray, memoryview


        -   Các toán tử trong Python
            1, Toán tử số học - Arithmetic Operators.
                +)  Toán tử "+" : Toán tử cộng các giá trị lại với nhau 
                +)  Toán tử "-" : Toán tử trừ các giá trị lại với nhau	
                +)  Toán tử "*" : Toán tử nhân các giá trị lại với nhau	
                +)  Toán tử "/" : Toán tử chia các giá trị cho nhau	
                +)  Toán tử "%" : Toán tử chia lấy phần dư 	
                +)  Toán tử "**" : Toán tử mũ. a**b = ab
                +)  Toán tử "//" : Toán tử chia làm tròn xuống.


            2, Toán tử Quan hệ.
                +)  Toán tử "==" : So sánh giá trị của các đối số xem có bằng nhau hay không.
                                    Nếu bằng nhau thì kết quả trả về sẽ là True và ngược lại sẽ là False.

                +)  Toán tử "!=" : So sánh giá trị của các đối số xem có khác nhau hay không.
Nếu khác nhau thì kết quả trả về sẽ là True và ngược lại sẽ là False.	

                +)  Toán tử "<" : Dấu < đại diện cho phép toán nhỏ hơn, nếu đối số 1 nhỏ hơn đối số 2 thì kết quả sẽ trả về là True và ngược lại sẽ là False.	

                +)  Toán tử ">" : Dấu > đại diện cho phép toán lớn hơn, nếu đối số 1 lớn hơn đối số 2 thì kết quả sẽ trả về là True và ngược lại sẽ là False.

                +)  Toán tử "<=" : Dấu > đại diện cho phép toán nhỏ hơn hoặc bằng, nếu đối số 1 nhỏ hơn hoặc bằng đối số 2 thì kết quả sẽ trả về là True và ngược lại sẽ là False.

                +)  Toán tử ">=" : Dấu > đại diện cho phép toán lớn hơn hoặc bằng, nếu đối số 1 lớn hơn hoặc bằng đối số 2 thì kết quả sẽ trả về là True và ngược lại sẽ là False.
                
            3, Toán tử gán.
                +)  Toán tử "=" : Toán tử này dùng để gán giá trị của một đối tượng cho một giá trị
                +)  Toán tử "+=" : Toán tử này cộng rồi gắn giá trị cho đối tượng	
                +)  Toán tử "-=" : Toán tử này trừ rồi gắn giá trị cho đối tượng	
                +)  Toán tử "*=" : Toán tử này nhân rồi gắn giá trị cho đối tượng	
                +)  Toán tử "/=" : Toán tử này chia rồi gắn giá trị cho đối tượng	
                +)  Toán tử "%" : Toán tử này lũy thừa rồi gắn giá trị cho đối tượng
                +)  Toán tử "//=" : Toán tử này chia làm tròn rồi gắn giá trị cho đối tượng


            4, Toán tử logic.

                +)  Toán tử "and" : Nếu 2 vế của toán tử này đều là True thì kết quả sẽ là True và ngược lại nếu 1 trong 2 vế là False thì kết quả trả về sẽ là False.

                +)  Toán tử "or" : Nếu 1 trong 2 vế là True thì kết quả trả về sẽ là True và ngược lại nếu cả 2 vế là False thì kết quả trả về sẽ là False.

                +)  Toán tử "not" : Đây là dạng phủ định, nếu biểu thức là True thì nó sẽ trả về là False và ngược lại.
	

            5, Toán tử biwter.

                - Toán tử này khá ít được sử dụng nên chỉ liệt kê thôi ạ , cụ thể như : 
                    +)  Toán tử "&" 
                    +)  Toán tử "|"
                    +)  Toán tử "^"
                    +)  Toán tử "~"
                    +)  Toán tử "<<"
                    +)  Toán tử ">>"

            6, Toán Tử khai thác.

                -   Toán tử này thường được dùng để kiểm tra xem 1 đối số có nằm trong 1 tập hợp đối số hay không (list). Trong Python hỗ trợ chúng ta 2 dạng toán tử như sau:

                Giả sử: a = 4, b = [1,5,7,6,9]

                +)  Toán tử "in" : Nếu 1 đối số thuộc một tập đối số nó sẽ trả về True và ngược lại
                    Ví dụ : a in b //False
                +)  Toán tử "not in" : Nếu 1 đối số không thuộc một tập đối số nó sẽ trả về True và ngược lại
                    Ví dụ : a not in b //True


            7, Toán tử xác thực.    

                -   Dạng Toán tử này dùng để xác thực hai giá trị xem nó có bằng nhau hay không. Và trong Python hỗ trợ chúng ta 2 dạng sau:

                Giả sử: a = 4, b =5

                +)  Toán tử "is" : Toán tử này sẽ trả về True nếu a == b và ngược lại 
                    Ví dụ :  a is b //False
                +)  Toán tử "not is" : Toán tử này sẽ trả về True nếu a != b và ngược lại
                    Ví dụ : a is not b //True