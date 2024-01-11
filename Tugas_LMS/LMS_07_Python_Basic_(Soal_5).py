'''
Soal 5: Pemahaman List Comprehension dan Fungsi

- Buatlah sebuah fungsi even_square_numbers(n) yang menggunakan list comprehension untuk menghasilkan 
list bilangan kuadrat dari bilangan genap antara 1 hingga n.

- Panggil fungsi even_square_numbers dengan nilai n tertentu untuk menghasilkan list bilangan kuadrat 
dari bilangan genap sampai nilai n.
'''

def even_square_numbers(n):
    # Menghasilkan list bilangan kuadrat dari bilangan genap antara 1 hingga n
    even_squares = [x**2 for x in range(2, n+1, 2)]  # Menggunakan range(2, n+1, 2) untuk mendapatkan bilangan genap
    return even_squares

# Panggil fungsi even_square_numbers dengan nilai n tertentu
n_value = 10
result = even_square_numbers(n_value)

# Menampilkan hasil
print(f"Bilangan kuadrat dari bilangan genap antara 1 hingga {n_value}: {result}")