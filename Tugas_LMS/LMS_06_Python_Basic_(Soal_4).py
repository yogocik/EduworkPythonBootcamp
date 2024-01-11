'''
Soal 4: Manipulasi Dictionary dan Fungsi

- Buatlah sebuah fungsi count_characters(string) yang menghitung jumlah kemunculan setiap karakter 
dalam sebuah string dan mengembalikan hasilnya dalam bentuk dictionary.

- Berikan sebuah string sebagai input dan panggil fungsi count_characters untuk menghitung jumlah 
kemunculan setiap karakter dalam string tersebut.
'''

def count_characters(string): # membuat fungsi baru yang menerima parameter 'string'
    char_count = {}  # membuat dictionary kosong sebagai tempat menyimpan jumlah kemunculan karakter
    for char in string: # looping
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Memberikan string sebagai input
input_string = "Indonesia wkwk land"

# Memanggil fungsi count_characters
result = count_characters(input_string)

# Menampilkan hasil
print("String Input:", input_string)
print("Jumlah Kemunculan Setiap Karakter:", result)