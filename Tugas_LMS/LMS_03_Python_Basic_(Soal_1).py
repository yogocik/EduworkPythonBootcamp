'''
Soal 1: Manipulasi List dan Fungsi
- Buatlah sebuah fungsi find_average(numbers) yang menerima sebuah list bilangan dan mengembalikan nilai 
rata-rata dari bilangan-bilangan tersebut.
- Buat list angka acak sebagai input dan panggil fungsi find_average untuk menghitung rata-ratanya.
'''

import random

def find_average(numbers):
    if not numbers:
        return 0  # Mengembalikan 0 jika list kosong untuk menghindari pembagian dengan nol
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Membuat list angka acak sebagai input
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Memanggil fungsi find_average
average_result = find_average(random_numbers)

# Menampilkan hasil
print("List Angka:", random_numbers)
print("Rata-rata:", average_result)

