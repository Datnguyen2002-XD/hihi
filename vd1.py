# def Nhap_HS():
#     n = int(input("Mời nhập số học sinh: "))
#     A = []
#     for i in range(n):
#         ht = input("Nhập họ tên học sinh thứ "+str(i+1)+": ")
#         A.append(ht)
#     return A
# #Hàm xuất danh sách
# def Xuat_HS(A):
#     for i in range(len(A)):
#         print(i+1,"\t",A[i])
# #Chương trình chính
# A = Nhap_HS()
# Xuat_HS(A)
class sinhvien:
    masv = "01";
    hoten = "ng a";
    def nhap():
        masv = input("nhap msv");
        hoten = input("nhap ten");
    def xuat(self):
        print("ho va ten :", self.hoten);
n = int(input("nhap so luong sinh vien:"))
sv = []
for i in range(0, n):
    s = sinhvien();
    s.nhap();
    sv.append(s.masv+s.hoten);