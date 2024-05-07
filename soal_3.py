def soal_3():
    def kalkulator_total(jumlah_barang):
        total_harga = 0
        for banyak in range(jumlah_barang):
            harga = float(input("Masukkan harga barang ke-{}: ".format(banyak+1)))
            total_harga += harga
        return total_harga

    jumlah_barang = int(input("Masukkan jumlah barang: "))
    total_belanjaan = kalkulator_total(jumlah_barang)

    print("Total belanjaan: Rp.{:.0f}".format(total_belanjaan))
soal_3()