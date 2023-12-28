
# Switch
print("\n SWITCH")
#contoh dari fitur yang disebut "pattern matching" atau "switch case" yang saya gunakan untuk pemilihan outfit kerja sesuai dengan hari kerja
Hari = "Jum'at" #input nilai akan di cocokan dengan beberapa kondisi
match Hari: #statement yang membandingkan nilai input dengan beberapa pola 'Case". 
    case "Senin": #jika di salah satu di antara case dapat terpenuhi oleh nilai input hari maka akan diprint hasil Outfit yang akan digunakan pada hari tsb.
        print("Kemeja Putih + Celana chinos Cokelat")
    case "Selasa":
        print("Kemeja Cokelat + Celana kain Hitam")
    case "Rabu":
        print("Kemeja Biru sky + Denim + outer crewneck")
    case "Kamis":
        print("Kemeja Batik + Celana chinos Biru donker")
    case "Jum'at":
        print("Baju Kokoh + Celana chinos hitam")

    case _: # apabila dari semua case di atas tidak cocok dengan input hari maka akan di print hasil selain case hari
        print("tidak ada format")

# TRY-CATCH, EXCEPTION

def calculate_rice_distribution(total_rice, total_people):
    try:
        res = total_rice / total_people
        print(f"It's fair distribution, each person shall receive {res:.0f} kg rice")
    except ZeroDivisionError as e:
        print(f"Operation not allowed -> divide by zero")
print("\n EXCEPTION, TRY_CATCH")
calculate_rice_distribution(100, 5)
calculate_rice_distribution(25, 0)

# Branching

def tahun_kabisat(tahun): #Fungsi ini menerima satu parameter, yaitu tahun dengan tipe int.
    if tahun % 4 == 0: #kondisi-1 untuk menghitung tahun dengan modulus 4.
        if tahun % 100 == 0: #kondisi-2 apabila kondisi-1 terpenuhi akan dijalankan.
            if tahun % 400 == 0: #kondisi-3 dijalankan jika kondisi-2 terpenuhi.
                print("Tahun Kabisat") #jika kondisi 1, 2 dan 3 terpenuhi maka input tahun adalah tahun kabisat. 
            else:
                print("Bukan Tahun Kabisat") #jika kondisi 1 dan 2 saja yang terpenuhi maka bukan tahun kabisat.
        else:
            print("Tahun Kabisat") #jika kondisi 2 tidak terpenuhi maka input Tahun adalah Tahun Kabisat.
    else :
        print("bukan Tahun Kabisat") #jika kondisi 1 tidak terpenuhi maka bukan merupakan Tahun Kabisat.

print("\n BRANCHING")
tahun_kabisat(2020)

# Loop untuk menghitung jumlah bilangan ganjil dari 1 hingga 50

jumlah_ganjil = 0

for i in range(1,51,2):
    if i % 2 != 0:
        jumlah_ganjil += 1

print("\n LOOP")
print(f"Jumlah bilangan ganjil dari 1 hingga 50 adalah: {jumlah_ganjil}")

# Class

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius **2
    

rectangle_obj = Rectangle(10, 15)
circle_obj = Circle(7)

# Memanggil metode calculate_area() pada objek yang berbeda
area_rectangle = rectangle_obj.calculate_area()
area_circle = circle_obj.calculate_area()
# hasil
print("\n POLYMORPHISM")
print(f"Area of Rectangle: {area_rectangle}")
print(f"Area of Circle: {area_circle}")

# Inheritances

class Vehicle:
    def __init__(self, type, sales, year):
        self.type = type
        self.sales = sales
        self.year = year
    def product(self):
        print(f"{self.type} {self.year}")

class Car(Vehicle):
    def __init__(self, type, sales, year):
        super().__init__(type, sales, year)
class Bicycle(Vehicle):
    def __init__(self, type, sales, year):
        super().__init__(type, sales, year)

car1 = Car("Mazda", 100, 2022)
car2 = Car("Honda", 50, 2019)

bi1 = Bicycle("BMX", 129, 2002)
bi2 = Bicycle("Folding Bike", 23, 2020)

#Inheritance concept using "product method" from main class Vehicle in Sub-Class Car and Bicycle
print("\n INHERITANCES")
car1.product() 
bi2.product()

# Encacpsulations

class Person():
    def __init__(self, first, last, age):
        self.first = first
        self.age = age
        self.last = last
        self._species = "Human"
    def FullName(self):
        print(f"{self.first} {self.last}")

per1 = Person("Abizar", "Adi", 24)
per2 = Person("Masayu", "Indah", 20)

print("\n ENCAPSULATION")
print(per1._species)

