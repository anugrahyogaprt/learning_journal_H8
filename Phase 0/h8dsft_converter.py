'''
~ This is Non-Graded Challange 2 for Anugrah Yoga Pratama - Batch 10 Data Science by Hacktiv8 ~

- Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin.
- Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit.
Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin. Panggil function yang pertama jika diperlukan.
- Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. Berikan argumen untuk memastikan bahwa outputnya dalah celcius atau kelvin.
- Berikan dokumentasi pada setiap baris kode yang kalian tulis.

'''

#Fungsi 1 - Konversi Celcius ke Kelvin
def c_to_k(celcius):
    kelvin = celcius + 273.15
    return kelvin

#Fungsi 2 - Konversi Kelvin ke Celcius
def k_to_c(kelvin):
    celcius = kelvin - 273.15
    return celcius

# #Fungsi 3 - Konversi C/K ke Fahrenheit (Unit equals C or K)
def ck_to_f(temp , unit):
    if unit == 'C' or unit == 'K':
        if unit == 'C' and temp > -273.15:
            tempF = temp * 9/5 + 32
            print("Temperature in Fahrenheit is {:.2f} °F". format(tempF))
        elif unit == 'K' and temp > 0:
            tempF = k_to_c(temp) * 9/5 + 32
            print("Temperature in Fahrenheit is {:.2f} °F". format(tempF))
        elif unit == 'C': 
            print("Celcius value must be greater than -273.15 °C")
        else:
            print("Kelvin value must be greater than 0 K")

    else:
        print("Unit must be 'C' or 'K'")

#Jalankan fungsi 3
ck_to_f(373.15, 'K')

#Fungsi 4 - Konversi Fahrenheit ke C dan K
def f_to_ck(temp_F):
    tempC = (temp_F - 32) * 5/9
    tempK = c_to_k(tempC)
    if tempC > -273.15 and tempK > 0:
        print("Temperature in Celcius is {:.2f} °C". format(tempC))
        print("Temperature in Kelvin is {:.2f} K". format(tempK))
    else:
        print("Fahrenheit value must be greater than -459.67")
#Jalankan fungsi 4
f_to_ck(212)