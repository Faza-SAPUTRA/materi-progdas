# Materi 1 - Operator

# operator aritmatika
a = 15
b = 4

print(a + b)    # penjumlahan
print(a - b)    # pengurangan
print(a * b)    # perkalian
print(a / b)    # pembagian (hasilnya float)
print(a // b)   # pembagian bulat
print(a % b)    # modulus (sisa bagi)
print(a ** b)   # pangkat

# prioritas operator
print(2 + 3 * 4)        # 14, bukan 20
print((2 + 3) * 4)      # 20

# operator assignment
x = 10
x += 5      # x = x + 5
x -= 3      # x = x - 3
x *= 2      # x = x * 2
print(x)

# operator perbandingan (hasilnya True/False)
print(10 == 10)     # sama dengan
print(10 != 5)      # tidak sama dengan
print(10 > 5)       # lebih besar
print(10 < 5)       # lebih kecil
print(10 >= 10)     # lebih besar atau sama
print(10 <= 20)     # lebih kecil atau sama

# operator logika
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# contoh pakai logika
umur = 20
punya_ktp = True
boleh_masuk = umur >= 17 and punya_ktp
print(f"Boleh masuk? {boleh_masuk}")

nilai = 50
lulus = nilai >= 60 or nilai == 50
print(f"Lulus? {lulus}")
