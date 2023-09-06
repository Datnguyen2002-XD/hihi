# class person:
#     hoten = "a";
#     tuoi = 10;
#     def __init__(self, hoten, tuoi):
#         self.hoten = hoten;
#         self.tuoi = tuoi;
# p1 = person();
# print(p1.hoten);
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

def main():
    num_students = int(input("Nhập số lượng sinh viên: "))
    students = []
    
    for i in range(num_students):
        print(f"\nNhập thông tin cho sinh viên thứ {i+1}:")
        student_id = input("Mã sinh viên: ")
        student_name = input("Họ tên sinh viên: ")
        
        student = Student(student_id, student_name)
        students.append(student)
    
    print("\nThông tin các sinh viên:")
    for student in students:
        print(f"Mã SV: {student.student_id}, Họ tên: {student.student_name}")

if __name__ == "__main__":
    main()