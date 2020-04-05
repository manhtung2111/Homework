class Days_of_month:  # khai báo 1 lớp
    def month(self, m):  # khởi tạo hàm month và có thuộc tính m
        if m in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
            print("This month have 31 days")
        elif m in ("April", "September", "June", "November"):
            print("This month have 30 days")
        elif m == "February":
            y = int(input("Please input a year that you need to know how many days in Feb:"))
            # cách tính năm nhuận để đưa ra số ngày trong tháng 2 chuẩn nhất
            if (y % 4) == 0:
                if (y % 100) == 0:
                    if (y % 400) == 0:
                        print("In", y, ", February have 29 Days")
                    else:
                        print("In", y, ", February have 28 Days")
                else:
                    print("In", y, ", February have 29 Days")
            else:
                print("In", y, ", February have 28 Days")


x = str(input("Input the month you like the most:"))
Days_of_month().month(x)
