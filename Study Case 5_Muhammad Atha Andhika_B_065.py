print("-Sistem Pemesanan Hotel-")
print("\nSelamat Datang di Hotel Atha5Stars!")

def hitung_biaya(tipe_kamar, lama_nginap):
    if tipe_kamar == "Standard":
        tarif = 200000

    elif tipe_kamar == "Deluxe":
        tarif = 350000

    else:
        tarif = 0

    totalbiaya = tarif * lama_nginap
    return totalbiaya

def validasitgl(tanggal=""):

    if "-" not in tanggal:
        return False

    bagian = tanggal.split("-")

    if len(bagian) != 3:
        return False

    if bagian[0].isdigit() and bagian[1].isdigit() and bagian[2].isdigit():

        hari = int(bagian[0])
        bulan = int(bagian[1])
        tahun = int(bagian[2])

        if tahun < 2026:
            return False

        elif bulan < 1 or bulan > 12:
            return False

        elif bulan == 2:
            if hari >= 1 and hari <= 29:
                return True
            else:
                return False

        elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
            if hari >= 1 and hari <= 30:
                return True
            else:
                return False

        else:
            if hari >= 1 and hari <= 31:
                return True
            else:
                return False
    
    return False

while True:
    nama = input("Masukkan nama penyewa: ").strip()
    if nama == "":
        print("Nama tidak boleh kosong! Mohon memasukkan nama!")

    else:
        break

while True:
    tipe_kamar = input("Masukkan tipe kamar (Standard/Deluxe): ").strip()
    tipe_kamar = tipe_kamar.lower()
    if tipe_kamar == "":
        print("Input tipe kamar tidak boleh kosong!")

    elif tipe_kamar == "standard":
        tipe_kamar = "Standard"
        break

    elif tipe_kamar == "deluxe":
        tipe_kamar = "Deluxe"
        break

    else:
        print("Tipe kamar tidak valid! Pilih antara Standard/Deluxe.")

while True:
    tanggalcheckin = input("Masukkan tanggal check-in (DD-MM-YYYY): ").strip()
    if tanggalcheckin == "":
        print("Tanggal check-in tidak boleh kosong!")

    elif validasitgl(tanggalcheckin):

        tanggalcheckout = input("Masukkan tanggal check-out (DD-MM-YYYY): ").strip()
        if tanggalcheckout == "":
            print("Tanggal check-out tidak boleh kosong!")

        elif validasitgl(tanggalcheckout):

            hari_checkin = int(tanggalcheckin.split("-")[0])
            bulan_checkin = int(tanggalcheckin.split("-")[1])
            tahun_checkin = int(tanggalcheckin.split("-")[2])

            hari_checkout = int(tanggalcheckout.split("-")[0])
            bulan_checkout = int(tanggalcheckout.split("-")[1])
            tahun_checkout = int(tanggalcheckout.split("-")[2])

            lama_nginap = (
                (tahun_checkout - tahun_checkin) * 360
                + (bulan_checkout - bulan_checkin) * 30
                + (hari_checkout - hari_checkin)
            )

            if lama_nginap <= 0:
                print("Minimal nginap 1 malam! Tanggal check-out harus setelah check-in!")

            elif lama_nginap > 30:
                print("Lama menginap maksimal 30 malam!")

            else:
                break
        else:
            print("Format atau tanggal check-out tidak valid! Gunakan DD-MM-YYYY.")
    else:
        print("Format atau tanggal check-in tidak valid! Gunakan DD-MM-YYYY.")

totalbiaya = hitung_biaya(tipe_kamar, lama_nginap)

if tipe_kamar == "Standard":
    tarif = 200000

else:
    tarif = 350000

print()
print("==========DETAIL PEMESANAN HOTEL==========")
print("Nama Penyewa      :", nama)
print("Tipe Kamar        :", tipe_kamar)
print("Tanggal Check-In  :", tanggalcheckin)
print("Tanggal Check-Out :", tanggalcheckout)
print("Lama Menginap     :", lama_nginap, "malam")
print("Tarif Kamar       : Rp", tarif, "/ malam" )
print("Total Biaya       : Rp", totalbiaya)
