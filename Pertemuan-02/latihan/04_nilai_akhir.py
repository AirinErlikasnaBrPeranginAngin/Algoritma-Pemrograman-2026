nama = input ("Masukkan nama: ")
tugas = float (input("Masukkan nilai tugas: "))
uts = float(input ("Masukkan nilai UTS: "))
uas = float (input ("Masukkan nilai UAS: "))

nilai_akhir = (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)

print (f"Nama: {nama}")
print (f"Nilai akhir: {nilai_akhir:.2}")