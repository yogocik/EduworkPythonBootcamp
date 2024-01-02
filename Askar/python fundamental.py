# SOAL 1: Manipulasi list dan Fungsi

# fungsi rata-rata
def find_average(numbers):
    if not numbers:
        return "List is empty."
    
    # rumus mean/rata-rata
    total = sum(numbers)
    average = total / len(numbers)

    return average

# contoh penerapan pada list
my_numbers = [5, 12, 7, 6, 10]
result = find_average(my_numbers)

print(f"Rata-rata dari list {my_numbers} adalah: {result}\n")

# SOAL 2: Pemahaman String dan Fungsi

# Fungsi reversed words
def reverse_words(sentence):
    reversed_words = sentence[::-1]

    return reversed_words

# contoh penerapan reverse words
original_sentence = "Belajar Python Askar"
reversed_result = reverse_words(original_sentence)

print(f"Kalimat Asli: {original_sentence}")
print(f"Kalimat Terbalik: {reversed_result}\n")

# SOAL 3: Pemahaman Data Casting dan Fungsi
def convert_temperature(degrees, from_unit, to_unit):
    """
    Convert temperature from one unit to another.

    Parameters:
    - degrees (float): The temperature value to be converted.
    - from_unit (str): The unit of the input temperature ('C', 'F', or 'K').
    - to_unit (str): The unit to which the temperature should be converted ('C', 'F', or 'K').

    Returns:
    float: The converted temperature.
    """

    # Function to convert Celsius to Fahrenheit
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    # Function to convert Fahrenheit to Celsius
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    # Function to convert Celsius to Kelvin
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    # Function to convert Kelvin to Celsius
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    
      # Function to convert Fahrenheit to Kelvin
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    # Function to convert Kelvin to Fahrenheit
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

    # Convert the input temperature to Celsius for standardization
    if from_unit == 'F':
        degrees_celsius = fahrenheit_to_celsius(degrees)
    elif from_unit == 'K':
        degrees_celsius = kelvin_to_celsius(degrees)
    else:
        degrees_celsius = degrees

    # Convert Celsius to the desired output unit
    if to_unit == 'F':
        result = celsius_to_fahrenheit(degrees_celsius)
    elif to_unit == 'K':
        result = celsius_to_kelvin(degrees_celsius)
    else:
        result = degrees_celsius

    return result

# Example usage:
temperature_in_celsius = 25.0
temperature_in_fahrenheit = 37.0
temperature_in_kelvin = 350.0

converted_temperature = convert_temperature(temperature_in_kelvin, 'K', 'C')
converted_temperature_1 = convert_temperature(temperature_in_celsius, 'C', 'K')
converted_temperature_2 = convert_temperature(temperature_in_fahrenheit, 'F', 'C')
converted_temperature_3 = convert_temperature(temperature_in_celsius, 'C', 'F')
converted_temperature_4 = convert_temperature(temperature_in_fahrenheit, 'F', 'K')
converted_temperature_5 = convert_temperature(temperature_in_kelvin, 'K', 'F')

print(f"{temperature_in_kelvin} degrees kelvin is {converted_temperature:.2f} degrees celsius")
print(f"{temperature_in_celsius} degrees celsius is {converted_temperature_1:.2f} degrees kelvin")
print(f"{temperature_in_fahrenheit} degrees fahrenheit is {converted_temperature_2:.2f} degrees celsius")
print(f"{temperature_in_celsius} degrees celsius is {converted_temperature_3:.2f} degrees fahrenheit")
print(f"{temperature_in_fahrenheit} degrees fahrenheit is {converted_temperature_4:.2f} degrees kelvin")
print(f"{temperature_in_kelvin} degrees kelvin is {converted_temperature_5:.2f} degrees fahrenheit\n")

# SOAL 4: Manipulasi Dictionary dan Fungsi
def count_characters(string):
    """
    Count the occurrences of each character in the given string.

    Parameters:
    - string (str): The input string.

    Returns:
    dict: A dictionary where keys are characters, and values are their respective counts.
    """
    character_count = {}

    for char in string:
        # Increment the count for each character or set it to 1 if not present
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

# Example usage:
input_string = "Nama saya askar"
result = count_characters(input_string)

for key in result:
    print(f"Character {key} occurs {result[key]} times.")

# SOAL 5: Manipulasi Dictionary dan 

def even_square_numbers(n):
    list = []
    # return number
    for n in range(0, 10):
        # print(num)
        if n % 2 == 0:
            list.append(n * n)
            
    return list

print(even_square_numbers(20))