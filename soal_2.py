def soal_2():
    def cek_tahun(tahun):
        if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
            return True
        else:
            return False
        
    tahun = int(input("Masukkan tahun: "))
    if cek_tahun(tahun):
        print("=="*22)
        print(f"tahun {tahun} merupakan TAHUN KABISAT")
        print("=="*22)
    else:
        print("=="*22)
        print(f"tahun {tahun} merupakan BUKAN TAHUN KABISAT")
        print("=="*22)
soal_2()