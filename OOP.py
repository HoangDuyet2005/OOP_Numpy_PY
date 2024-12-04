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