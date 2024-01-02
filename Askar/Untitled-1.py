# SOAL 1: Manipulasi list dan Fungsi

def find_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return average

number = [2,4,1,7,9,13]
result = find_average(number)
# print(f"Rata-rata dari {number} adalah {result}\n")

# SOAL 2: Pemahaman String dan Fungsi

def reverse_words(sentence):
    reverse_words = sentence[::-1]

    return reverse_words

my_sentence = "Belajar Python Askar"
result = reverse_words(my_sentence)

# print(f"Kalimat Normal: {my_sentence}")
# print(f"Kalimat Terbalik: {result}\n")

# SOAL 3: Pemahaman Data Casting dan Fungsi

def convert_temperature(deegres, from_unit, to_unit):
    def celsius_to_fahrenheit(deegres):
        celsius_to_fahrenheit = (celsius * 9/5) + 32

        return celsius_to_fahrenheit
    
    def fahrenheit_to_celsius(deegres):
        fahrenheit_to_celsius = (fahrenheit - 32) * 5/9

        return fahrenheit_to_celsius
    
    if from_unit == 'C':
        deegres = celsius_to_fahrenheit(deegres)
    elif from_unit == 'F':
        deegres = fahrenheit_to_celsius(deegres)

    return deegres

    if to_unit == 'F':
        deegres = celsius_to_fahrenheit(deegres)
    elif to_unit == 'C':
        deegres = fahrenheit_to_celsius(deegres)
        
    return deegres
    
celsius = 30
fahrenheit = 75

convert_from_celsius = convert_temperature(celsius,'C','F')
convert_from_fahrenheit = convert_temperature(fahrenheit,'F','C')

# print(f"nilai dari {celsius} derajat celsius adalah {convert_from_celsius} derajat fahrenheit")
# print(f"nilai dari {fahrenheit} derajat fahrenheit adalah {convert_from_fahrenheit:.2f} derajat celsius")







