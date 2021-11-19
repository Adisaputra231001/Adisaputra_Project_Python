print("Selamat Datang di ATM saya")
print("Pilih Option :")
print("1. Check Uang Saya")
print("2. Ambil Uang Saya")
print("3. Tabung Uang saya")
option=int(input("Silahkan pilih option :"))
if option==1:
    print("Uang kamu Berjumlah Rp.450.000")
elif option==2:
    print("Uang Kamu Berjumlah Rp.450.000, Mau tarik berapa?")
    print("1. Rp.100.000")
    print("2. Rp.200.000")
    print("3. Rp.450.000")
    uang_kamu=450000
    option2=int(input("Option :"))
    if option2==1:
        hasil=uang_kamu-100000
        print("Uang Kamu Sekarang Berjumlah :",hasil)
    elif option==2:
        hasil2=uang_kamu-200000
        print("Uang Kamu Sekarang Berjumlah :",hasil2)
    elif option==3:
        hasil3=uang_kamu-450000
        print("Uang Kamu Sekarang Berjumlah :",hasil3)
    else:
        print("Keyword Anada Salah")
elif option==3:
    uang_kamu=450000
    print("Uang berjumlah Rp.450.000, Mau Nabung Berapa?")
    option3=int(input("Masukan Jumlah Uang :"))
    hasil4=uang_kamu+option3
    print("Jumlah Uang kamu Sekarang Adalah ",hasil4)
else:
    print("Keyword Anda salah, Mohon coba lagi")

