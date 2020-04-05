class temperature:  # Khai báo 1 lớp
    def __init__(self, temp):  # khởi tạo thuộc tính temo có trong class
        self.temp = temp

    def convert(self):

        degree = int(self.temp[:-1])  # phần tử từ vị trí đầu đến vị trí gần cuối
        i_convention = self.temp[-1]  # phần tử ở vị trí cuối cùng trong 1 string
        if i_convention.upper() == "C":  # viết hoa
            result = int(round(9 * degree) / 5 + 32)  # làm tròn phép chia
            o_convention = "Farenheit"
        elif i_convention.upper() == 'F':
            result = int(round((degree - 32) * 5 / 9))
            o_convention = "Celsius"
        else:
            print("Can't convert this temperature")
            exit() #thông báo k convert được và thoát chương trình, không chạy tiếp câu lệnh sau

        print("The temperature in", o_convention, "is", result, "degrees.")


x = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ") #nhập giá trị nhiệt độ cần convert
this_temperature = temperature(x) #khởi tạo 1 object this_temperature
this_temperature.convert() # gọi hàm convert
