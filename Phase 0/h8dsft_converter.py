'''
~ This is Non-Graded Challange 2 for Anugrah Yoga Pratama - Batch 10 Data Science by Hacktiv8 ~

- Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin.
- Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit.
Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin. Panggil function yang pertama jika diperlukan.
- Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. Berikan argumen untuk memastikan bahwa outputnya dalah celcius atau kelvin.
- Berikan dokumentasi pada setiap baris kode yang kalian tulis.

'''

def kelvin_to_celcius(temp_k):
    temp_c = temp_k - 273.15
    print(temp_c)
    return temp_c

def celcius_to_kelvin(temp_c):
    temp_k = temp_c + 273.15
    print(temp_k)
    return temp_k

def CelcKelv_to_fahrenheit(temp_c = 0, temp_k = 0):
    temp_fc = 9/5*(temp_c) + 32
    temp_fk = 9/5*(kelvin_to_celcius(temp_k)) + 32
    print(temp_fc, " and ", temp_fk)

celcius_to_kelvin(285.273)
kelvin_to_celcius(60.85)
CelcKelv_to_fahrenheit(100)