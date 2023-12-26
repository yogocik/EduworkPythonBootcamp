
# # Manipulasi List dan fungsi

def find_average(number):
    return sum(number) / len(number)

number = [141,54,12,8,40]
hasil = find_average(number)
print("\n LIST & FUNGSI")
print("List angka acak: ->", number)
print("Average result: ->", hasil)

# Pemahaman str dan fungsi
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

kalimat_asli = "Aku cukup produktif hari ini"
kalimat_terbalik = reverse_words(kalimat_asli)

print("\n STRING & FUNGSI")
print(f"kalimat asli : ", kalimat_asli)
print(f"kalimat reversed : ", kalimat_terbalik)

# Data Casting (Temperature Conversion)

def convert_temperature(degrees, from_unit, to_unit):
    if from_unit == to_unit:
        return degrees
    if from_unit == "C" and to_unit == "F":
        return degrees *  9/5 + 32
    elif from_unit== "C" and to_unit== "K":
        return degrees + 273.15
    
    elif from_unit == "F" and to_unit == "C":
        return (degrees - 32) * 5/9
    elif from_unit == "F" and to_unit== "K":
        return (degrees - 32) * 5/9 + 273.15

    elif from_unit =="K" and to_unit == "C":
        return degrees - 273.15
    elif from_unit== "K"and to_unit == "F":
        return (degrees - 273.15) * 9/5 + 32


    else:
        print("unit tidak dikenal")
        return None


C_to_F = convert_temperature(45, "C", "F")
C_to_K = convert_temperature(45, "C", "K")


print("\n DATA CASTING & FUNGSI")
print(f"hasil konversi C -> F: {C_to_F}")    
print(f"hasil konversi C -> K: {C_to_K}")

# Manipulasi Dictionary dan Fungsi

def count_characters(string):
    counts = dict()
    chars = string.split()

    for character in chars:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts
            
print("\n DICTIONARY & FUNGSI")
print(count_characters("Hello World, I am from Indonesia, where are you guys from ?"))

# LIST Comprehension dan FUngsi

def even_square_numbers(n):
    squares = [x**2 for x in range(2, n+1, 2) ]

    return squares
print("\n LIST COMPRE & FUNGSI")
print(even_square_numbers(8))
