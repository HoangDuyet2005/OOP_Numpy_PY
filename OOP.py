class Person:
    #class attributes(chung cho mọi đối tượng trong lớp)
    nationality='Viet Nam'
    def __init__(self,name,job,salary):
    #instance attributes(mỗi đối tượng có thuộc tính riêng)
        self.name = name #public
        self.job = job #public
        self.__salary = salary #private
    #class method(phương thức chung cho tất cả đối tượng)
    def greet(self):
        print('Xin chao')
    def infor(self):
        print(self.name+' '+self.job)
    #để đảm bảo nên để private và trong lớp viết hàm để truy cập tới
    def get_name(self):
        return self.name
    def get_job(self):
        return self.job
    def set_name(self, name):
        self.name = name
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary=salary
if __name__=='__main__':
    p1=Person('Duyet','Data engineer or software engineer',1000)
    p2=Person('Chi','Logisticer',1000)
    print(p1.nationality, p1.name, p1.job)
    print(p2.  nationality, p2.name, p2.job)
    p1.greet()
    p2.greet()
    p1.infor()
    #print(p1.__salary) (không truy cập vì private chỉ bên trong lớp mới được)
    print(p1.get_salary())#lấy ra
    p1.set_salary(2000)# đưu vào
    print(p1.get_salary())
    #Nên để tất cả thuộc tính private còn phương thức public
    #Nên viết hàm get set để lấy và thay đổi giá trị
class SoPhuc:
    def __init__(self,thuc,ao):
        self.thuc=thuc
        self.ao=ao
    def __add__(self, other):
        a=self.thuc+other.thuc
        b=self.ao+other.ao
        return SoPhuc(a,b)
    def __str__(self):
        return f'{self.thuc}+{self.ao}j'
if __name__=='__main__':
    s1=SoPhuc(1,1)
    s2=SoPhuc(2,2)
    s3=s1+s2
    print(s3)
#Kế thừa
class Person:
    def __init__(self):
        print('constructor')
    def gioithieu(self):
        print('đây là lớp cha')
class Student(Person):
    def __init__(self):
        super().__init__() 
        #Hoặc có 1 cách khác là Person.__init__(thuộc tính của lớp cha)
        #Gọi lại tên lớp cha. hoặc từ khóa super().
        print('Hàm khởi tạo của lớp con')
if __name__=='__main__':
    sv=Student()
    sv.gioithieu()
#kế, đa
#Cha
class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def gioi_thieu(self):
        print("HÊ NÔ, tao là", self.ten, "tao", self.tuoi, "tuổi.")
#con1
class GiaoVien(Nguoi):
    def __init__(self, ten, tuoi, mon_day):
        super().__init__(ten, tuoi)
        self.mon_day = mon_day
    def gioi_thieu(self):
        print("Tao là GV", self.ten, ", tao dạy ", self.mon_day, "tao", self.tuoi, "tuổi.")
#con2
class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, nganh_hoc):
        super().__init__(ten, tuoi)
        self.nganh_hoc = nganh_hoc
    def gioi_thieu(self):
        print("Tao là SV ", self.ten, ", tôi học ", self.nganh_hoc, "tao", self.tuoi, "tuổi.")
#đa hình
def gioi_thieu_chung(doi_tuong):
    doi_tuong.gioi_thieu()
#tao doi tuong tu cac lop khac nhau
gv = GiaoVien("Thầy Tỉnh", 50, "OOP Java")
sv = SinhVien("Duyệt", 19, "Kĩ thuật phẩn mềm")
nguoi = Nguoi("Hoàng Thế Duyệt", 19)
# Gọi phương thức gioi_thieu qua hàm chung
gioi_thieu_chung(gv)
gioi_thieu_chung(sv)
gioi_thieu_chung(nguoi)
#Ghi đè
class Person:
    def __init__(self,name,job):
        self.name=name
        self.job=job
    def show(self):
        return f'{self.name} {self.job}'
class Studen(Person):
    def __init__(self, name, job, salary):
        super().__init__(name, job)
        self.salary=salary
    def show(self):
        #return super().show()+ ' '+f'{self.salary}' #Cách 1
        return Person.show(self)+f' {self.salary}' #Cách 2
if __name__=='__main__':
    sv=Studen('Duyet','dev',1000)
    print(sv.show())
#Trừu tượng
from abc import ABC, abstractmethod
# Tạo một lớp trừu tượng
class Animal(ABC):
    # Phương thức trừu tượng
    @abstractmethod
    def speak(self):
        pass 
    #Phương thức thông thường
    def move(self):
        print("This animal moves!")
#Lớp cụ thể kế thừa lớp trừu tượng
class Dog(Animal):
    def speak(self):
        print("Gâu!")
class Cat(Animal):
    def speak(self):
        print("Mèo méo meo mèo meo")
#Tạo đối tượng từ lớp cụ thể
dog = Dog()
dog.speak()
dog.move()
cat = Cat()
cat.speak()


