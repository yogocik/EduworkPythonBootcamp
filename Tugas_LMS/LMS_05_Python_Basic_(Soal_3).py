'''
Soal 3: Pemahaman Data Casting dan Fungsi

- Buatlah sebuah fungsi convert_temperature(degrees, from_unit, to_unit) yang mengonversi suhu dari 
unit yang diberikan (from_unit) ke unit lainnya (to_unit). Parameter degrees adalah nilai suhu, dan 
from_unit serta to_unit dapat berupa "C" untuk Celsius, "F" untuk Fahrenheit, atau "K" untuk Kelvin.

- Uji fungsi convert_temperature dengan nilai suhu dan unit yang berbeda untuk melihat konversinya.
'''

def convert_temperature(degrees, from_unit, to_unit):
    if from_unit == to_unit:
        return degrees  # Jika unit awal dan unit tujuan sama, tidak perlu konversi

    if from_unit == "C":
        if to_unit == "F":
            return (degrees * 9/5) + 32  # Konversi dari Celsius ke Fahrenheit
        elif to_unit == "K":
            return degrees + 273.15  # Konversi dari Celsius ke Kelvin

    elif from_unit == "F":
        if to_unit == "C":
            return (degrees - 32) * 5/9  # Konversi dari Fahrenheit ke Celsius
        elif to_unit == "K":
            return (degrees + 459.67) * 5/9  # Konversi dari Fahrenheit ke Kelvin

    elif from_unit == "K":
        if to_unit == "C":
            return degrees - 273.15  # Konversi dari Kelvin ke Celsius
        elif to_unit == "F":
            return (degrees * 9/5) - 459.67  # Konversi dari Kelvin ke Fahrenheit

    # Jika unit tidak valid
    raise ValueError("Unit tidak valid. Gunakan 'C', 'F', atau 'K'.")

# Uji fungsi convert_temperature dengan beberapa contoh
temperature_celsius = 25.0
converted_to_fahrenheit = convert_temperature(temperature_celsius, "C", "F")
converted_to_kelvin = convert_temperature(temperature_celsius, "C", "K")

print(f"{temperature_celsius} Celsius sama dengan {converted_to_fahrenheit:.2f} Fahrenheit")
print(f"{temperature_celsius} Celsius sama dengan {converted_to_kelvin:.2f} Kelvin")
