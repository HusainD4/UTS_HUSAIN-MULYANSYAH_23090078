def soal_1():

    print("=="*22)
    print("SELAMAT DATANG DI PROGRAM")
    print("MENGHITUNG PENJUMLAHAN,PENGURANGAN, DAN MODULUS")
    print("=="*22)

    def operasi_aritmatika():
        bil_pertama = int(input("Masukkan bilangan pertama: "))
        bil_kedua = int(input("Masukkan bilangan kedua: "))

        print("=="*22)
        hasil_penjumlahan = bil_pertama + bil_kedua
        print("Hasil penjumlahan:", hasil_penjumlahan)
        hasil_pengurangan = bil_pertama - bil_kedua
        print("Hasil pengurangan:", hasil_pengurangan)
        hasil_modulus = bil_pertama % bil_kedua
        print("Hasil modulus:", hasil_modulus)
        print("=="*22)
    operasi_aritmatika()
    print("=="*22)
    print("TERIMAKSIH TELAH MENGGUNAKAN PROGRAM SAYA")
    print("=="*22)

soal_1()    
