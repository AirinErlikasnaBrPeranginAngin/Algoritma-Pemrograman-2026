TAHUN_SEKARANG = 2026
nama = input ("Masukkan nama: ")
nim = input ("Masukkan NIM: ")
kelas = input ("Masukkan kelas: ")
tahun_lahir = int (input ("Masukkan tahun lahir: "))
umur = TAHUN_SEKARANG - tahun_lahir 
print ("=== BIODATA MAHASISWA ===") 
print (f"nama : {nama}")
print (f"NIM : {nim}")
print (f"Kelas : {kelas}")
print (f"Umur : sekitar {umur} tahun")