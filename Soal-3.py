a = float(input("Nilai teori anda : "))
b = float(input("Nilai praktikum anda: "))
if a >= 70 and b >= 70:
    print("Selamat, anda lulus!")
elif a >= 70 and b < 70:
    print("Anda harus mengulang ujian praktek")
elif a < 70 and b >= 70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")