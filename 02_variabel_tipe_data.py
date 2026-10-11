# Materi 1 - Variabel dan Tipe Data

# variabel
nama = "Budi"
umur = 18
tinggi = 170.5
is_mahasiswa = True

print(nama, umur, tinggi, is_mahasiswa)

# cek tipe data pakai type()
print(type(nama))
print(type(umur))
print(type(tinggi))
print(type(is_mahasiswa))

# konversi tipe data (type casting)
angka_str = "100"
angka_int = int(angka_str)
print(angka_int + 50)

umur = 18
print("Umur saya " + str(umur) + " tahun")

# f-string
nama = "Budi"
umur = 18
print(f"Nama: {nama}, Umur: {umur}")
print(f"Tahun lahir: {2026 - umur}")

# input selalu string, harus di-cast kalau mau angka
nama = input("Nama: ")
umur = int(input("Umur: "))
ipk = float(input("IPK: "))

print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"IPK: {ipk:.2f}")
