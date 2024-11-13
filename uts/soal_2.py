def cek_tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False

# Contoh penggunaan
tahun = int(input("Masukkan tahun: "))
if cek_tahun_kabisat(tahun):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")