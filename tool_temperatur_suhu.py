print('ALAT KONVERSI TEMPERATUR')
print('='*30)

while True:
    UserInput = int(input('Pilih Temperatur :\n\n1.Celcius\n2.Reamur\n3.Fahrenheit\n4.Kelvin\n\nPilih no berapa: '))
    if (UserInput == 1):
        celcius = float(input('Masukan Suhu Dalam Celcius: '))
        reamur = 4/5*celcius
        print('\nSuhu Dalam Reamur: ',reamur)
        fahrenheit = (9/5*celcius)+32
        print("="*30,'\nSuhu Dalam Fahrenheit: ',fahrenheit)
        kelvin = celcius+273
        print("="*30,'\nSuhu Dalam Kelvin: ',kelvin)
    elif (UserInput == 2):
        reamur_a = float(input('Masukan Suhu Dalam Reamur: '))
        celcius_a = 5/4*reamur_a
        print('\nSuhu Dalam Celcius: ',celcius_a)
        fahrenheit_a = (9/4*reamur_a)+32
        print("="*30,'\nSuhu Dalam Fahrenheit: ',fahrenheit_a)
        kelvin_a = (5/4*reamur_a)+273
        print("="*30,'\nSuhu Dalam Kelvin: ',kelvin_a)
    elif (UserInput == 3):
        fahrenheit_b = float(input('Masukan Suhu Dalam Fahrenheit: '))
        celcius_b = 5/9*(fahrenheit_b-32)
        print('\nSuhu Dalam Celcius: ',fahrenheit_b)
        reamur_b = 4/9*(fahrenheit_b-32)
        print('\nSuhu Dalam Reamur: ',reamur_b)
        kelvin_b = (celcius_b)+273
        print('\nSuhu Dalam Kelvin: ',kelvin_b)
    elif (UserInput == 4):
        kelvin_c = float(input('Masukan Suhu Dalam Kelvin: '))
        celcius_c = kelvin_c-273
        print('\nSuhu Dalam Celcius: ',celcius_c)
        reamur_c = 4/5*(kelvin_c-273)
        print('\nSuhu Dalam Reamur: ',reamur_c)
        fahrenheit_c = (9/5*(celcius_c))+32
        print('\nSuhu Dalam Fahrenheit: ',fahrenheit_c)
    else:
        break
   
    

    
