trying = 0 #mewakili berapa kali coba
secret_number = 7 # angka rahasia
limit = 3 # bnyk kesempatan

while trying < limit:
    angka_masukan = input("masukkan angka 1-9 : ")
    angka_masukan = int(angka_masukan)

    if angka_masukan == secret_number:
         print("selamat, kamu menang")
         break

    trying += 1