'''
Soal 2: Pemahaman String dan Fungsi
- Buatlah sebuah fungsi reverse_words(sentence) yang menerima sebuah kalimat dan mengembalikan kalimat 
tersebut dengan urutan kata-kata dibalik.
-Berikan sebuah kalimat sebagai input dan panggil fungsi reverse_words untuk membalik urutan kata-kata 
dalam kalimat tersebut.
'''

def reverse_words(sentence):
    words = sentence.split()  # Memisahkan kata-kata dalam kalimat
    reversed_sentence = ' '.join(reversed(words))  # Membalik urutan kata-kata dan menggabungkannya kembali
    return reversed_sentence

# Memberikan kalimat sebagai input
input_sentence = "wkwkwkwk, ini adalah contoh kalimat"

# Memanggil fungsi reverse_words
reversed_result = reverse_words(input_sentence)

# Menampilkan hasil
print("Kalimat Asli:", input_sentence)
print("Kalimat terbalik:", reversed_result)