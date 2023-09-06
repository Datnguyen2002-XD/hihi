print("hello world");
#dong coment
a = 10;
b = 2.3;
s = "xin chao";
#khai bao ham (vd1)
def tinhtong(x, y):
    return x+y;
tinhtong(3, 4);
print("tong cua hai so x va y la:", tinhtong(3, 4));
#khai bao ham(nhap vao tu ban phim)
x = int(input("nhap x:"));
y = int(input("nhap y:"));
print("tong cua hai so x va y la:", tinhtong(x, y));

x = float(input("nhap x:"));
y = float(input("nhap y:"));
print("tong cua hai so x va y la:", tinhtong(x, y));

if(x<y):
    print("x nho hon y");
elif(x==y):
    print("x bang y");
elif(x>y):
    print("x lon hon y");

s = input("nhap vao chuoi: ")
for i in range(0, len(s)):
    print(i);

#nhap vao so sinh vien tu ban phim
#nhap thong tin cho tung sinh vien tu ban phim
#in ra danh sach sinh vien